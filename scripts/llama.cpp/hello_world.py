import os

from llama_cpp import Llama
from pyprojroot import here

model_path = os.path.join(here(), "model", "tinyllama-2-1b-miniguanaco.Q2_K.gguf")

# Instanciate the model
my_aweseome_llama_model = Llama(model_path=model_path, n_gpu_layers=-1)


prompt = "This is a prompt"
max_tokens = 100
temperature = 0.3
top_p = 0.1
echo = True
stop = ["Q", "\n"]


while True:
    # Define the parameters
    model_output = my_aweseome_llama_model(
        prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        echo=echo,
        stop=stop,
    )
    final_result = model_output["choices"][0]["text"].strip()

    print(final_result)