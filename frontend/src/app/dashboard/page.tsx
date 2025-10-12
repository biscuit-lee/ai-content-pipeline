'use client'
import { signOut, useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { useState, useEffect } from "react"

export default function Dashboard() {
  const { data: session, status } = useSession()
  const router = useRouter()
  
  // States
  const [stories, setStories] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedStory, setSelectedStory] = useState(null)
  
  // Handle auth redirect
  useEffect(() => {
    if (status === "loading") return
    if (!session) {
      router.push('/')
    }
  }, [session, status, router])

  // Load user stories on mount
  useEffect(() => {
    if (session) {
      loadUserStories()
    }
  }, [session])

  // Show loading state
  if (status === "loading") {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-purple-600"></div>
      </div>
    )
  }

  if (!session) {
    return <div>Redirecting...</div>
  }

  const handleSignOut = () => {
    signOut({ callbackUrl: '/' })
  }

  const loadUserStories = async () => {
    try {
      const response = await fetch('/api/stories')
      if (response.ok) {
        const data = await response.json()
        setStories(data.stories || mockStories) // Use mock data for demo
      }
    } catch (error) {
      console.error('Error loading stories:', error)
      setStories(mockStories) // Fallback to mock data
    } finally {
      setLoading(false)
    }
  }

  const handleCreateNew = () => {
    router.push('/create-story') // Redirect to story generator
  }

  const handleViewStory = (story) => {
    setSelectedStory(story)
  }

  const handleCloseModal = () => {
    setSelectedStory(null)
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  }

  const getStoryTypeEmoji = (type) => {
    const emojiMap = {
      'adventure': '🗺️',
      'mystery': '🔍',
      'romance': '💕',
      'sci-fi': '🚀',
      'fantasy': '🧙‍♂️',
      'horror': '👻',
      'comedy': '😂',
      'drama': '🎭',
      'thriller': '⚡',
      'children': '🧸'
    }
    return emojiMap[type] || '📚'
  }

  // Mock data for demonstration
  const mockStories = [
    {
      id: 1,
      title: "The Magical Portal",
      type: "fantasy",
      prompt: "A young wizard discovers a magical portal in their backyard",
      content: "In the quiet suburbs of Willowbrook, twelve-year-old Emma had always thought her backyard was ordinary. The old oak tree, the rusty swing set, and the patch of wildflowers seemed like nothing special. But on this particular Tuesday evening, as golden sunlight filtered through the leaves, Emma noticed something extraordinary...",
      audioUrl: "/audio/story1.mp3",
      createdAt: "2024-12-15T10:30:00Z",
      status: "completed"
    },
    {
      id: 2,
      title: "Murder at the Manor",
      type: "mystery", 
      prompt: "A detective must solve a locked-room murder at a Victorian mansion",
      content: "Detective Sarah Chen pulled her coat tighter as she approached Blackwood Manor. The Victorian mansion loomed against the stormy sky, its Gothic windows seeming to watch her every move. Inside, a puzzle awaited that would challenge everything she thought she knew about impossible crimes...",
      audioUrl: "/audio/story2.mp3",
      createdAt: "2024-12-14T16:45:00Z",
      status: "completed"
    },
    {
      id: 3,
      title: "Love in the Coffee Shop",
      type: "romance",
      prompt: "Two strangers keep meeting at the same coffee shop",
      content: "The morning rush at Brew & Books was Maya's favorite time of day. Not because she enjoyed crowds, but because that's when he came in. The tall stranger with kind eyes who always ordered the same thing: medium coffee, black, with a blueberry muffin...",
      audioUrl: null,
      createdAt: "2024-12-13T09:15:00Z",
      status: "draft"
    },
    {
      id: 4,
      title: "Space Station Omega",
      type: "sci-fi",
      prompt: "Astronauts discover an alien signal from deep space",
      content: "Commander Lisa Park was reviewing the daily reports when the proximity alarm shattered the quiet hum of Space Station Omega. What appeared on the main screen would change humanity's understanding of our place in the universe forever...",
      audioUrl: "/audio/story4.mp3",
      createdAt: "2024-12-12T14:20:00Z",
      status: "completed"
    }
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Top Navigation */}
      <nav className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <div className="flex items-center space-x-3">
                <div className="w-8 h-8 bg-purple-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-sm">📚</span>
                </div>
                <h1 className="text-xl font-semibold text-gray-900">Story Generator</h1>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-3">
                <img 
                  src={session.user?.image || '/default-avatar.png'} 
                  alt="Profile" 
                  className="h-8 w-8 rounded-full"
                />
                <span className="text-sm font-medium text-gray-700">
                  {session.user?.name || session.user?.email}
                </span>
              </div>
              <button
                onClick={handleSignOut}
                className="ml-4 px-4 py-2 rounded-lg text-sm font-medium 
                          text-gray-600 bg-gray-100 hover:bg-gray-200 hover:text-gray-800 
                          shadow-sm hover:shadow-md transition-all duration-200 ease-in-out"
              >
                Sign Out
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <div className="px-4 py-6 sm:px-0">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">
              Welcome back, {session.user?.name?.split(' ')[0] || 'Storyteller'}! ✨
            </h2>
            <p className="text-lg text-gray-600 mb-6">Ready to create your next masterpiece?</p>
            
            {/* Create New Story Button */}
            <button
              onClick={handleCreateNew}
              className="inline-flex items-center px-8 py-4 bg-purple-600 text-white text-lg font-medium rounded-xl hover:bg-purple-700 shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200"
            >
              <svg className="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              Create New Story
            </button>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div className="bg-white overflow-hidden shadow-lg rounded-xl">
              <div className="p-6">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-12 h-12 bg-purple-500 rounded-xl flex items-center justify-center">
                      <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-4">
                    <p className="text-sm font-medium text-gray-500">Total Stories</p>
                    <p className="text-2xl font-bold text-gray-900">{stories.length}</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow-lg rounded-xl">
              <div className="p-6">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
                      <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-4">
                    <p className="text-sm font-medium text-gray-500">Completed</p>
                    <p className="text-2xl font-bold text-gray-900">{stories.filter(s => s.status === 'completed').length}</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow-lg rounded-xl">
              <div className="p-6">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-12 h-12 bg-yellow-500 rounded-xl flex items-center justify-center">
                      <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-4">
                    <p className="text-sm font-medium text-gray-500">Drafts</p>
                    <p className="text-2xl font-bold text-gray-900">{stories.filter(s => s.status === 'draft').length}</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow-lg rounded-xl">
              <div className="p-6">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
                      <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-4">
                    <p className="text-sm font-medium text-gray-500">Audio Stories</p>
                    <p className="text-2xl font-bold text-gray-900">{stories.filter(s => s.audioUrl).length}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Stories Grid */}
          <div className="mb-8">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-2xl font-bold text-gray-900">Your Stories</h3>
              <div className="flex space-x-2">
                <button className="px-4 py-2 text-sm font-medium text-purple-600 bg-purple-100 rounded-lg hover:bg-purple-200 transition-colors">
                  All Stories
                </button>
                <button className="px-4 py-2 text-sm font-medium text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors">
                  Completed
                </button>
                <button className="px-4 py-2 text-sm font-medium text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors">
                  Drafts
                </button>
              </div>
            </div>

            {loading ? (
              <div className="flex justify-center py-12">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-600"></div>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {stories.map((story) => (
                  <div key={story.id} className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-200 overflow-hidden">
                    <div className="p-6">
                      <div className="flex items-start justify-between mb-3">
                        <div className="flex items-center space-x-2">
                          <span className="text-2xl">{getStoryTypeEmoji(story.type)}</span>
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800 capitalize">
                            {story.type}
                          </span>
                        </div>
                        <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                          story.status === 'completed' 
                            ? 'bg-green-100 text-green-800' 
                            : 'bg-yellow-100 text-yellow-800'
                        }`}>
                          {story.status}
                        </span>
                      </div>
                      
                      <h4 className="text-lg font-semibold text-gray-900 mb-2 line-clamp-1">
                        {story.title}
                      </h4>
                      
                      <p className="text-sm text-gray-600 mb-3 line-clamp-2">
                        {story.prompt}
                      </p>
                      
                      <p className="text-sm text-gray-500 mb-4">
                        Created {formatDate(story.createdAt)}
                      </p>

                      <div className="flex space-x-2">
                        <button
                          onClick={() => handleViewStory(story)}
                          className="flex-1 bg-purple-600 text-white py-2 px-4 rounded-lg text-sm font-medium hover:bg-purple-700 transition-colors"
                        >
                          View Story
                        </button>
                        {story.audioUrl && (
                          <button className="bg-green-100 text-green-700 py-2 px-3 rounded-lg text-sm font-medium hover:bg-green-200 transition-colors">
                            🎧
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Story Modal */}
      {selectedStory && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-xl max-w-4xl max-h-[90vh] overflow-y-auto">
            <div className="p-6 border-b border-gray-200">
              <div className="flex justify-between items-center">
                <div>
                  <h3 className="text-2xl font-bold text-gray-900">{selectedStory.title}</h3>
                  <div className="flex items-center space-x-3 mt-2">
                    <span className="text-lg">{getStoryTypeEmoji(selectedStory.type)}</span>
                    <span className="capitalize text-purple-600 font-medium">{selectedStory.type}</span>
                    <span className="text-gray-400">•</span>
                    <span className="text-gray-500">{formatDate(selectedStory.createdAt)}</span>
                  </div>
                </div>
                <button
                  onClick={handleCloseModal}
                  className="text-gray-400 hover:text-gray-600"
                >
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>
            
            <div className="p-6">
              <div className="mb-6">
                <h4 className="font-semibold text-gray-900 mb-2">Original Prompt:</h4>
                <p className="text-gray-600 bg-gray-50 p-3 rounded-lg">{selectedStory.prompt}</p>
              </div>
              
              <div className="mb-6">
                <h4 className="font-semibold text-gray-900 mb-2">Story:</h4>
                <div className="text-gray-700 leading-relaxed font-serif">
                  {selectedStory.content.split('\n').map((paragraph, index) => (
                    <p key={index} className="mb-3">{paragraph}</p>
                  ))}
                </div>
              </div>

              {selectedStory.audioUrl && (
                <div className="mb-6 bg-purple-50 p-4 rounded-lg">
                  <h4 className="font-semibold text-gray-900 mb-2">🎧 Audio Version:</h4>
                  <audio controls className="w-full">
                    <source src={selectedStory.audioUrl} type="audio/mpeg" />
                    Your browser does not support the audio element.
                  </audio>
                </div>
              )}

              <div className="flex space-x-3 pt-4 border-t border-gray-200">
                <button className="flex-1 bg-purple-600 text-white py-2 px-4 rounded-lg font-medium hover:bg-purple-700 transition-colors">
                  Edit Story
                </button>
                {selectedStory.audioUrl && (
                  <button className="bg-green-100 text-green-700 py-2 px-4 rounded-lg font-medium hover:bg-green-200 transition-colors">
                    Download Audio
                  </button>
                )}
                <button 
                  onClick={handleCloseModal}
                  className="bg-gray-100 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-200 transition-colors"
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}