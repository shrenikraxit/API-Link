from openai import OpenAI


client = OpenAI(api_key="sk-HcSk5O-BU0b_pbq-BHvcrVqRhKcBK-BpLr2Std9VdET3BlbkFJ3en0RRQ8aPUMJmPqVl0geC1Mvye3KSnEhpQ1To6aQA")



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
            "url": "https://drive.google.com/file/d/1zobAk-OkN_BPwUs-rEoHVvtsgtSeLeyn/view?usp=drive_link",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])


