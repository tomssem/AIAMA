import os

from llama_cpp import Llama
from pyprojroot import here

model_path = os.path.join(here(), "model", "tinyllama-2-1b-miniguanaco.Q2_K.gguf")

# Instanciate the model
llm = Llama(model_path=model_path, n_gpu_layers=-1)

# llm = Llama.from_pretrained(
#     repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF",
#     filename="*q8_0.gguf",
#     verbose=True,
#     n_gpu_layers=-1,
# )


prompt = "This is a prompt that" * 10
max_tokens = 100
temperature = 10
top_p = 10
echo = True
stop = ["Q", "\n"]


# Define the parameters
model_output = llm(
    prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    echo=echo,
    stop=stop,
)
final_result = model_output["choices"][0]["text"].strip()

print(final_result)