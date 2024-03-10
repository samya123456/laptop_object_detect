from vertexai.preview.generative_models import GenerativeModel, Part
import base64


def generate():
    prompt = """

Predict the age, sex, and correctness of the sitting posture.

Please provide your prediction based on the provided video feed.
For the sitting posture, if the the person is sitting straight with the backbone straight, then sitting posture is correct
otherwise the sitting posture is incorrect.
"""
    file_path = 'output.mp4'
    print(file_path)
    encrypt_data = encode_video_to_base64(file_path)
    video1 = Part.from_data(data=base64.b64decode(
        encrypt_data), mime_type="video/mp4")
    model = GenerativeModel("gemini-pro-vision")
    responses = model.generate_content(
        [video1, prompt],
        generation_config={
            "max_output_tokens": 1024,
            "temperature": 0,
            "top_p": 1,
            "top_k": 32
        },
        stream=False,
    )

    # print('response =', responses)
    print('responses.candidate = ',
          responses.candidates[0].content.parts[0].text)


def encode_video_to_base64(video_file_path):
    try:
        # Read the video file in binary mode
        with open(video_file_path, 'rb') as video_file:
            # Read the binary content of the video file
            video_binary_data = video_file.read()

        # Encode the binary data using Base64
        video_base64 = base64.b64encode(video_binary_data).decode('utf-8')

        return video_base64

    except FileNotFoundError:
        print(f"Error: The file '{video_file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
