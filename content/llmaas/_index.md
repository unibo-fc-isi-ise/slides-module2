+++

title = "[ISE] LLM-as-a-Service"
description = "Background about using LLMs via Service Providers"
outputs = ["Reveal"]

+++

# Using LLMs via Service Providers

{{% import path="reusable/footer.md" %}}

---

## Outiline

### Key engineering aspects of LLM-as-a-Service

0. **On-premise** vs. **On-cloud** deployment
    - On-premise: the model is hosted and run on the _user's own infrastructure_, commonly via _containerized solutions_ (e.g. [Ollama](https://ollama.com/), [Docker's Model Runner](https://www.docker.com/products/model-runner/), etc.)
        + implies ad-hoc _hardware requirements_ (e.g. Nvidia GPUs, Apple Silicon) and technical expertise for setup and maintenance
        + the service provider is commonly the company providing the _containerized solution_, and making _models_ available for _download_ and use
        + most commonly, containerized solutions provide the same _API_ as the on-cloud service, to facilitate migration between the two deployment options
    - On-cloud: the model is hosted and run on the _service provider's infrastructure_, and accessed via _API calls_
        + implies _<u>no</u> hardware requirements_ for the user, but a _cost per usage_ (e.g. per token, per request, etc.)

1. **Service Provider**: several exist, with different offerings in terms of models, pricing, and features (e.g. [OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/), [Google](https://cloud.google.com/vertex-ai), [Microsoft](https://azure.microsoft.com/en-us/services/cognitive-services/), etc.)
    - the choice of the service provider can depend on several factors, including:
        + the availability of _specific models_ (e.g. GPT-4, Claude, Gemini, etc.)
        + the _pricing model_ and cost structure
        + the _features_ and _capabilities_ offered (e.g. fine-tuning, custom models, MCP support, etc.)

1. **HTTP API "Type"** 

1. **Client Library**

---

{{% import path="reusable/back.md" %}}
