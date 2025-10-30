import boto3
import uuid
import os
from dotenv import load_dotenv
import requests
import whisper
from backend.prompts import group_scene_prompt

# Upload file and get URLs
def upload_audio_to_s3(audio_content, filename=None):
    try:
                
        load_dotenv()
        AWS_KEY    = os.getenv("AWS_ACCESS_KEY")
        AWS_SECRET = os.getenv("AWS_SECRET_KEY")
        AWS_REGION = os.getenv("AWS_REGION")
        BUCKET     = os.getenv("AWS_BUCKET_NAME")


        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET,
            region_name=AWS_REGION
        )

        # ADD THIS DEBUG
        print(f"🔍 DEBUG - BUCKET value: {BUCKET}")
        print(f"🔍 DEBUG - AWS_REGION value: {AWS_REGION}")
        

        # Generate unique filename if none provided
        if not filename:
            filename = f"audio/{uuid.uuid4()}.mp3"
        
        # Upload to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=filename,
            Body=audio_content,
            ContentType='audio/mpeg',
            CacheControl='max-age=3600'
        )
        
        # Generate presigned URL (temporary, secure)
        audio_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET, 'Key': filename},
            ExpiresIn=3600  # 1 hour expiration
        )
        
        # Generate download URL
        download_url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET, 
                'Key': filename,
                'ResponseContentDisposition': 'attachment; filename="story.mp3"'
            },
            ExpiresIn=3600
        )
        
        return {
            'success': True,
            'audioUrl': audio_url,
            'downloadUrl': download_url,
            'filename': filename
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }



def split_texts_by_paragraph(text: str) -> list:
    """
    Splits a long text into paragraphs based on double newlines.
    Returns a list of paragraphs.
    """
    paragraphs = [para.strip() for para in text.split("\n\n") if para.strip()]
    return paragraphs

def download_from_url(url, save_path):
    """Download a file from a download URL (from aws) and save it to the specified path."""
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return save_path
    else:
        raise Exception(f"Failed to download file from {url}, status code: {response.status_code}")

def upload_video_to_s3(video_path, filename=None):
    try:
                
        load_dotenv()
        AWS_KEY    = os.getenv("AWS_ACCESS_KEY")
        AWS_SECRET = os.getenv("AWS_SECRET_KEY")
        AWS_REGION = os.getenv("AWS_REGION")
        BUCKET     = os.getenv("AWS_BUCKET_NAME")


        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET,
            region_name=AWS_REGION
        )

        # ADD THIS DEBUG
        print(f"🔍 DEBUG - BUCKET value: {BUCKET}")
        print(f"🔍 DEBUG - AWS_REGION value: {AWS_REGION}")
        

        # Generate unique filename if none provided
        if not filename:
            filename = f"video/{uuid.uuid4()}.mp4"
        
        # Upload to S3
        with open(video_path, "rb") as video_file:
            s3.put_object(
                Bucket=BUCKET,
                Key=filename,
                Body=video_file,
                ContentType='video/mp4',
                CacheControl='max-age=3600'
            )
        
        # Generate presigned URL (temporary, secure)
        video_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET, 'Key': filename},
            ExpiresIn=3600  # 1 hour expiration
        )
        
        # Generate download URL
        download_url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET, 
                'Key': filename,
                'ResponseContentDisposition': 'attachment; filename="story.mp4"'
            },
            ExpiresIn=3600
        )
        
        return {
            'success': True,
            'videoUrl': video_url,
            'downloadUrl': download_url,
            'filename': filename
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


if __name__ == "__main__":
    # test split function
    sample_text = """
    There's a photograph from 1899. A mother sits in a pharmacy, holding her infant. On the counter between her and the pharmacist sits a small brown bottle. The label reads "Mrs. Winslow's Soothing Syrup—for teething babies." The pharmacist is smiling. The mother looks relieved.

What the photograph doesn't show is what's inside that bottle. Morphine. Enough morphine to kill the child if the mother follows the recommended dosage too carefully.

This isn't a story about evil. It's a story about ignorance masquerading as expertise. And it's the foundation of every pill in your medicine cabinet today.

Because modern medicine wasn't born from brilliance. It was born from a graveyard so large we stopped counting the bodies.

**[THESIS - 0:45-1:30]**

Here's what they don't teach you in biology class. Medical progress isn't a straight line from ignorance to knowledge. It's a maze walked by blind men, where every wrong turn costs lives, and the only way forward is trial, error, and an unfathomable amount of death.

For most of human history, going to a doctor was statistically more dangerous than staying home. The treatments killed more people than the diseases. But we didn't know that. We couldn't know that. Because without controlled studies, without statistical analysis, without any way to separate correlation from causation, medicine was just educated guessing.

And the cost of those guesses was paid in human lives.

**[THE BLOODLETTING PRINCIPLE - 1:30-3:30]**

Let's start with a practice so fundamental to medicine that it persisted for two thousand years. Bloodletting. The intentional draining of blood from sick patients.

The theory made perfect sense to the ancients. They observed that people with fevers often had flushed skin, which they interpreted as too much blood. They noticed that injuries that bled seemed to relieve pressure and pain. They reasoned, logically within their understanding of the world, that removing excess blood would restore balance to the body.

Hippocrates, the father of medicine, recommended it. Galen, whose medical texts dominated European medicine for over a millennium, systematized it into a comprehensive theory. Medieval physicians built their entire practice around it. It wasn't fringe medicine. It was the medicine.

Consider George Washington. December 1799. He wakes with a sore throat, probably a bacterial infection we could treat today with a week of antibiotics. His doctors arrive. They are the best physicians in America, trained in the most current medical knowledge of their time.

Over the next 24 hours, they drain nearly half his blood. Five pints, extracted deliberately, methodically, with the full confidence that this treatment will save his life. Washington dies that evening.

The infection didn't kill him. His doctors did.

But here's what makes this story so unsettling. His physicians weren't incompetent. They followed protocol. They did exactly what their training taught them. And when Washington died, they likely attributed it to the severity of his illness, not the treatment. Because they had no framework for understanding what actually happened.

    """
    paragraphs = split_texts_by_paragraph(sample_text)
    
