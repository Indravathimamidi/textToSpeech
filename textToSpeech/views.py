from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
def index(request):
  return render(request,'index.html')
def speech(request):
    if request.method == 'POST':
        text = request.POST.get('textInput')
        audio_file_path = os.path.join(settings.MEDIA_ROOT, 'output.mp3')
        text_to_speech(text,'en',audio_file_path)

        # Save or generate the audio file at the specified path

        # Construct the URL to the audio file
        audio_file_url = os.path.join(settings.MEDIA_URL, 'output.mp3')

        context = {
            'text': text,
            'audio_file_url': audio_file_url,
            'audio_display': "audio_display",
        }
        
        # Process the text as needed (e.g., convert to speech)
        # For demonstration, we'll just return the text in the response
        # return HttpResponse(f"Received text: {text}")
        return render(request, 'index.html', context)
    else:
        return HttpResponse("Invalid request method.")
from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='media/output.mp3'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech as an audio file
    tts.save(output_file)
