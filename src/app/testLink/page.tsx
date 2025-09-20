'use client'
import { UploadDropArea } from "../components/UploadDropArea"

export default function TestLinkPage() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50">

            <div className="max-w-lg w-full mx-4">
                <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">Upload Your File</h2>
                <UploadDropArea />
            </div>



        </div>

        

    )
}