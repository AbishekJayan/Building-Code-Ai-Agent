from google import genai
from google.genai import types
import pymupdf

def generate():
  client = genai.Client(
      vertexai=True,
      project="blueprint-analysis",
      location="global",
  )

  text1 = types.Part.from_text(text="""You are a building code compliance validation agent. You have access to the following building code JSON  for the city of Omaha.


Building Code JSON:-

{
  "energyConservation": {
    "windowToWallRatio": {
      "section": "1301.1.1",
      "min_threshold": 15,
      "requirement": "Must comply with Nebraska Energy Code if window-to-wall ratio exceeds 15%",
      "reference": "Page 6"
    }
  },
  "roofingAndDrainage": {
    "rainwaterDischarge": {
      "section": "1502.5",
      "minDischargeDistanceFt": 3,
      "propertyLineDistanceFt": 20,
      "requirement": "Rainwater must be discharged at least 3 feet from the foundation, parallel to the property line if within 20 feet of it",
      "reference": "Page 6"
    },
    "roofCovering": {
      "section": "1511.3.1.1",
      "restriction": "No re-covering for existing slate, clay, cement, asbestos-cement tile, or asphalt shingle roofs",
      "reference": "Page 6"
    },
    "roofLoads": {
      "section": "1607.13.2.1",
      "minLiveLoadPsf": 25,
      "requirement": "Ordinary roofs must be designed for a minimum live load of 25 psf",
      "reference": "Page 7"
    }
  },
  "geotechnical": {
    "collapsibleSoils": {
      "section": "1803.5.3",
      "requirement": "Evaluate presence and impact of collapsible soils on structural performance",
      "reference": "Page 10"
    }
  }
}

Task: Your task is to analyze the input construction blueprint image and check if it complies with the information given in the JSON.

Output Schema

{
  "up_to_code": True/False,
  "Reason": "If Up_to_code is false, provide an explanation as to where in the blueprint is not up to code. If there are multiple reasons, list all of them."
                               
}

Notes:-
* Do not return any text other than the given output JSON Format
* Only use the information provided to perform the analysis. Do not look for information anywhere else

Example output 1:
{
    "up_to_code":False,
    "Reason":"The roof live load is muh lower than the minimum of 25psf"
                               
}
                               
Example output 2: 
{
"up_to_code":False,
"Reason":"All aspects of the blueprint are upto code"
}
                 

                               """)
  image1 = pymupdf.open("static/SF-381.pdf")

  model = "gemini-2.5-pro"
  contents = [
    types.Content(
      role="user",
      parts=[
        text1,
        image1
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()