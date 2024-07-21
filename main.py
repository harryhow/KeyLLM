import openai
from keybert.llm import OpenAI
from keybert import KeyLLM

documents = [
    "I want to find all the checkbox styles and use case in our designs.",
    "I want to search the the recipient page that XXX designer shared before.",
    "I want to check the previous version of the Log in page.",
    "I want to find the design pages with account number details / data.",
    "I want to find the illustrations / icons / creative assets we used for empty state / success state / failed state / confirmation.",
    "I want to find the app version of the Setting page.",
    "I want to find the interaction of this design to see what’s being implemented now."
]

# Set up the OpenAI client
client = openai.OpenAI()

# Create your LLM with the client
llm = OpenAI(client=client)

# Load it in KeyLLM
kw_model = KeyLLM(llm)

# Extract keywords
keywords = kw_model.extract_keywords(documents)

# Print the results
for doc, kws in zip(documents, keywords):
    print(f"Document: {doc}")
    print(f"Keywords: {kws}\n")