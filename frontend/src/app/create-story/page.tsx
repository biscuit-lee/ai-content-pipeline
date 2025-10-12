'use client'
import { signOut, useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { useState, useEffect } from "react"

export default function Dashboard() {
  const { data: session, status } = useSession()
  const router = useRouter()
  
  // Form states
  const [prompt, setPrompt] = useState('')
  const [storyType, setStoryType] = useState('reddit')
  const [generatedStory, setGeneratedStory] = useState('')
  const [editedStory, setEditedStory] = useState('')
  const [audioUrl, setAudioUrl] = useState('')
  const [tmpJson, setTmpJson] = useState(null) 
  // Loading states
  const [isGenerating, setIsGenerating] = useState(false)
  const [isGeneratingAudio, setIsGeneratingAudio] = useState(false)
  const [tts_provider, setTtsProvider] = useState('elevenlabs')
  // Current step in the process
  const [currentStep, setCurrentStep] = useState('input') // 'input', 'story', 'audio'

  // Story type options
  const storyTypes = [
    { value: 'reddit', label: '🗺️ Reddit' },
    { value: 'biz', label: '⚡ Business psychology explainer' },
    { value: 'children', label: '🧸 Children\'s Story' }
  ]

  const tts_providers = [
    { value: 'elevenlabs', label: 'ElevenLabs' },
    { value: 'kokoro', label: 'Kokoro (Needs to be Locally deployed)' },
  ]

  // Handle auth redirect
  useEffect(() => {
    if (status === "loading") return
    if (!session) {
      router.push('/')
    }
  }, [session, status, router])

  // Show loading state
  if (status === "loading") {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  if (!session) {
    return <div>Redirecting...</div>
  }

  const handleSignOut = () => {
    signOut({ callbackUrl: '/' })
  }

  const handleGenerateStory = async () => {
    if (!prompt.trim()) return
    
    setIsGenerating(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/api/generate-story', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt.trim(),
          storyType,
        }),
      })
      
      if (response.ok) {
        const data = await response.json()
        setTmpJson(data)
        const storyLines = data.story.map(item => item.line).join('\n');
        setGeneratedStory(storyLines)
        setEditedStory(storyLines)
        setCurrentStep('story')
      } else {
        alert('Failed to generate story. Please try again.')
      }
    } catch (error) {
      console.error('Error generating story:', error)
      alert('An error occurred. Please try again.')
    } finally {
      setIsGenerating(false)
    }
  }

  const handleGenerateAudio = async () => {
    if (!editedStory.trim()) return
    
    setIsGeneratingAudio(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/api/generate-audio', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          story: tmpJson,
          ttsProvider: tts_provider,
        }),
      })
      
      if (response.ok) {
        const data = await response.json()
        console.log('Audio generation response:', data)
        setAudioUrl(data.audioUrl)

        console.log('Audio URL:', data.audioUrl)
        console.log('variable audioUrl:', audioUrl)
        setCurrentStep('audio')
      } else {
        alert('Failed to generate audio. Please try again.')
      }
    } catch (error) {
      console.error('Error generating audio:', error)
      alert('An error occurred. Please try again.')
    } finally {
      setIsGeneratingAudio(false)
    }
  }

  const handleStartNew = () => {
    setPrompt('')
    setStoryType('reddit')
    setGeneratedStory('')
    setEditedStory('')
    setAudioUrl('')
    setCurrentStep('input')
  }

  const handleBackToEdit = () => {
    setCurrentStep('story')
    setAudioUrl('')
  }

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

      <div className="max-w-4xl mx-auto py-6 sm:px-6 lg:px-8">
        {/* Progress Steps */}
        <div className="mb-8">
          <div className="flex items-center justify-center space-x-8">
            <div className={`flex items-center ${currentStep === 'input' ? 'text-purple-600' : currentStep === 'story' || currentStep === 'audio' ? 'text-green-600' : 'text-gray-400'}`}>
              <div className={`w-8 h-8 rounded-full flex items-center justify-center ${currentStep === 'input' ? 'bg-purple-600 text-white' : currentStep === 'story' || currentStep === 'audio' ? 'bg-green-600 text-white' : 'bg-gray-300 text-gray-600'}`}>
                1
              </div>
              <span className="ml-2 font-medium">Create Prompt</span>
            </div>
            <div className={`w-16 h-0.5 ${currentStep === 'story' || currentStep === 'audio' ? 'bg-green-600' : 'bg-gray-300'}`}></div>
            <div className={`flex items-center ${currentStep === 'story' ? 'text-purple-600' : currentStep === 'audio' ? 'text-green-600' : 'text-gray-400'}`}>
              <div className={`w-8 h-8 rounded-full flex items-center justify-center ${currentStep === 'story' ? 'bg-purple-600 text-white' : currentStep === 'audio' ? 'bg-green-600 text-white' : 'bg-gray-300 text-gray-600'}`}>
                2
              </div>
              <span className="ml-2 font-medium">Edit Story</span>
            </div>
            <div className={`w-16 h-0.5 ${currentStep === 'audio' ? 'bg-green-600' : 'bg-gray-300'}`}></div>
            <div className={`flex items-center ${currentStep === 'audio' ? 'text-purple-600' : 'text-gray-400'}`}>
              <div className={`w-8 h-8 rounded-full flex items-center justify-center ${currentStep === 'audio' ? 'bg-purple-600 text-white' : 'bg-gray-300 text-gray-600'}`}>
                3
              </div>
              <span className="ml-2 font-medium">Generate Audio</span>
            </div>
          </div>
        </div>

        {/* Step 1: Input Form */}
        {currentStep === 'input' && (
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-6">Create Your Story</h2>
            
            <div className="space-y-6">
              {/* Story Type Dropdown */}
              <div>
                <label htmlFor="story-type" className="block text-sm font-medium text-gray-700 mb-2">
                  Story Type
                </label>
                <select
                  id="story-type"
                  value={storyType}
                  onChange={(e) => setStoryType(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-purple-500 focus:border-purple-500"
                >
                  {storyTypes.map((type) => (
                    <option key={type.value} value={type.value}>
                      {type.label}
                    </option>
                  ))}
                </select>
              </div>

              {/* Prompt Input */}
              <div>
                <label htmlFor="prompt" className="block text-sm font-medium text-gray-700 mb-2">
                  Story Prompt
                </label>
                <textarea
                  id="prompt"
                  rows={4}
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  placeholder="Describe the story you'd like to generate... (e.g., 'A young wizard discovers a magical portal in their backyard')"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-purple-500 focus:border-purple-500"
                />
              </div>

              {/* Generate Button */}
              <button
                onClick={handleGenerateStory}
                disabled={!prompt.trim() || isGenerating}
                className="w-full bg-purple-600 text-white py-3 px-4 rounded-md hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed font-medium transition-colors"
              >
                {isGenerating ? (
                  <div className="flex items-center justify-center">
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                    Generating Story...
                  </div>
                ) : (
                  'Generate Story'
                )}
              </button>
            </div>
          </div>
        )}

        {/* Step 2: Story Editor */}
        {currentStep === 'story' && (
          <div className="bg-white shadow rounded-lg p-6">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-gray-900">Edit Your Story</h2>
              <button
                onClick={handleStartNew}
                className="text-purple-600 hover:text-purple-700 font-medium"
              >
                Start New Story
              </button>
            </div>

            <label htmlFor="tts-provider" className="block text-sm font-medium mt-5 text-gray-700 mb-2">
                  Choose a TTS Provider
            </label>
            <select
                  id="tts-provider"
                  value={tts_provider}
                  onChange={(e) => setTtsProvider(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-purple-500 focus:border-purple-500"
                >
                  {tts_providers.map((type) => (
                    <option key={type.value} value={type.value}>
                      {type.label}
                    </option>
                  ))}
                </select>
            
            <div className="space-y-6">
              {/* Story Editor */}
              <div>
                <label htmlFor="story-editor" className="block text-sm font-medium mt-5 text-gray-700 mb-2">
                  Your Story (Click to edit)
                </label>
                <textarea
                  id="story-editor"
                  rows={12}
                  value={editedStory}
                  readOnly
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-purple-500 focus:border-purple-500 font-serif text-base leading-relaxed"
                />
              </div>

              {/* Action Buttons */}
              <div className="flex space-x-4">
                <button
                  onClick={() => setCurrentStep('input')}
                  className="flex-1 bg-gray-200 text-gray-700 py-3 px-4 rounded-md hover:bg-gray-300 font-medium transition-colors"
                >
                  Back to Prompt
                </button>
                <button
                  onClick={handleGenerateAudio}
                  disabled={!editedStory?.trim?.() || isGeneratingAudio}
                  className="flex-1 bg-purple-600 text-white py-3 px-4 rounded-md hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed font-medium transition-colors"
                >
                  {isGeneratingAudio ? (
                    <div className="flex items-center justify-center">
                      <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                      Generating Audio...
                    </div>
                  ) : (
                    'Generate Audio'
                  )}
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Audio Player */}
        {currentStep === 'audio' && (
          <div className="bg-white shadow rounded-lg p-6">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-gray-900">Your Audio Story</h2>
              <button
                onClick={handleStartNew}
                className="text-purple-600 hover:text-purple-700 font-medium"
              >
                Create New Story
              </button>
            </div>
            
            <div className="space-y-6">
              {/* Audio Player */}
              {audioUrl && (
                <div className="bg-purple-50 rounded-lg p-6">
                  <h3 className="text-lg font-medium text-gray-900 mb-4">🎧 Listen to your story</h3>
                  <audio controls className="w-full">
                    <source src={audioUrl} type="audio/mpeg" />
                    Your browser does not support the audio element.
                  </audio>
                  
                  {/* Download Button */}
                  <div className="mt-4">
                    <a
                      href={audioUrl}
                      download="my-story.mp3"
                      className="inline-flex items-center px-4 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 transition-colors"
                    >
                      <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3M3 17V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
                      </svg>
                      Download MP3
                    </a>
                  </div>
                </div>
              )}

              {/* Story Preview */}
              <div className="bg-gray-50 rounded-lg p-4">
                <h3 className="text-lg font-medium text-gray-900 mb-2">Story Text:</h3>
                <div className="text-gray-700 font-serif leading-relaxed max-h-64 overflow-y-auto">
                  {editedStory.split('\n').map((paragraph, index) => (
                    <p key={index} className="mb-2">{paragraph}</p>
                  ))}
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex space-x-4">
                <button
                  onClick={handleBackToEdit}
                  className="flex-1 bg-gray-200 text-gray-700 py-3 px-4 rounded-md hover:bg-gray-300 font-medium transition-colors"
                >
                  Edit Story Again
                </button>
                <button
                  onClick={handleGenerateAudio}
                  disabled={isGeneratingAudio}
                  className="flex-1 bg-purple-600 text-white py-3 px-4 rounded-md hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed font-medium transition-colors"
                >
                  Regenerate Audio
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}