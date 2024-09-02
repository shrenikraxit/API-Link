from openai import OpenAI
import os

api_key = os.getenv("API_KEY")
client = OpenAI(api_key)



response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What is this sign in American Sign Language"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://media.istockphoto.com/id/93214254/photo/vervet-monkey-chlorocebus-pygerythrus.jpg?s=612x612&w=0&k=20&c=p0Pxilywbzh0Jcsobjv3zCUaT5IQ93eTOtre8He4W9A=",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])


