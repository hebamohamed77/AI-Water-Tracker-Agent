import os
from unittest import result
from langchain_openai import chatopenai
from langchain.schema import human_message
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

LLM=chatopenai.ChatOpenAI(model="gpt-4", temperature=0.5, openai_api_key=openai_api_key)

class waterIntakeAgent:
    def __init__(self):
        self.History = []

    def AnalyzeIntake(self , intake_ml):
        prompt=f"""
            you are a hydration assistant that helps users track their water intake.
            the user has consumed {intake_ml} ml of water today.
            provide hydration status and suggest if they need to drink more water or if they are well hydrated.
            """
        
        response = LLM.invoke([human_message(content=prompt)])
        self.History.append((prompt, response.content))

        return response.content
    

    if __name__ == "__main__":
        agent = waterIntakeAgent()
        intake_ml = 1500
        feedback = agent.AnalyzeIntake(intake_ml)
        print(f"Hydration Feedback: {feedback}")