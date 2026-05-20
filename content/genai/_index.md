+++

title = "[ISE] Generative AI 101"
description = "Gentle Introduction to Generative AI"
outputs = ["Reveal"]

+++

# Generative AI 101

{{% import path="reusable/footer.md" %}}

---

{{< slide id="intro" >}}

## __GenAI__: _Generative_ Artificial Intelligence

<!-- > [Systems based on] <br> -->
_AI_ algorithms capable of __automatically generating__ _content_, e.g.:
- _text_
- images
- audio and/or video
- [source] code
- ...

(cf. [Policy for the ethical and responsible use of Generative Artificial Intelligence in teaching and research activities](https://www.unibo.it/it/allegati/policy-per-un-uso-etico-e-responsabile-dell2019intelligenza-artificiale-generativa-nelle-attivita-di-didattica-e-ricerca/@@download/file/Policy-Generative-AI.pdf))

---

## GenAI through _Foundation Models_ (FM)

+ Large _neural networks_ that learn to _process_, _"understand"_, and _produce_ [not necessarily] __structured__ and __unstructured__ data
+ __trained__ on _large_ amounts of data, and with _large_ computational resources, to __do a bit of everything__
    - with the idea that they can later be __specialized__ for _specific tasks_

<br>
{{< image src="./foundation-models.png" max-h="60vh" alt="Foundation models concept">}}

---

## __Terminology__: Foundation Models vs. _Large Language Models_

{{< image src="./fm-vs-llm.webp" width="80%" max-h="70vh" alt="Venn diagram explaining how LLMs are a specific case of foundation models" link="https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404" >}}

---

## Basic Operation of LLMs

<!-- ![Next word prediction](./next-word-prediction.png) -->
{{< image src="./next-word-prediction.png" width="100%" max-h="70vh" alt="Next word prediction concept">}}

- LLMs have learned to __predict__ the _next word_ in a _text_ given the _previous context_
    * similar to the _predictive_ keyboard on mobile phones, but much more _complex_ and _powerful_
- In other words, LLMs have learned how to use __natural language__
- Foundation models can combine input/output text with other modalities (e.g. images, audio, video)
    * e.g. accepting text + image as input, and producing text + image as output, or any combination of these modalities
- This makes them very good at dealing with __unstructured__ data, either in input or output

---

## Language and Reasoning

- __Natural language__ helps people _communicate_

- It can be used to express _complex_ or _abstract_ concepts

- It can be used to _reason_ about _problems_ and _solutions_
    - however it admits __imprecisions__, due to _ambiguity_, variable interpretations, subjectivity, etc.



> Natural language allows LLMs to use __intuition__ in _reasoning_, like humans do
> <br> (thus __making mistakes__ like humans do)
- $\implies$ LLMs can be very confident in themselves, while saying _incorrect_, _imprecise_, or _made-up_ things

- better would be to combine LLMs with __symbolic__ AI tools, to get the best of both worlds 

---

## Analogy with Dual-system theory 

{{< image src="./dual-system.png" width="100%" max-h="70vh" alt="Dual-system theory concept">}}

(cf. [Thinking, Fast and Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow))

---

{{% section %}}

## GenAI with an _as-a-Service_ consumption model

{{< image src="./llm-concept.svg" width="100%" max-h="70vh" alt="'As-a-Service' consumption model for foundation models" >}}

---

## GenAI with an _as-a-Service_ consumption model

- __Cost__ models:
    + __subscription-based__: you pay a fixed monthly/annual _fee_ to access the service
        * it often still includes _usage_ limits
    + __usage-based__: you pay _in proportion_ to the actual use of the service

- __Consumption__ is measured based on the _computational effort_ required to serve the request:
    + processed _tokens_ (for text)
    + number of _requests_ made per unit of time (minute, hour, day, month)
    + _size_ of the processed data (for images, audio, video)
    + _complexity_ of the specific _model_ used to serve the request

- __Generation__ should be considered a _stochastic_ process by construction

{{% fragment %}}
> - The __quality__ of the service is subject to randomness and _fluctuations_ due to:
>    + service _load_
>    + model choice, and its related _updates_
>    + service _limits_ possibly reached in the current _time window_
>    + chance
{{% /fragment %}}

{{% /section %}}

---

{{% section %}}

## GenAI _learning_ cycle

{{< image src="./dataflow.svg" width="100%" max-h="70vh" alt="GenAI learning cycle" >}}

---

## GenAI _learning_ cycle — __Consequences__ (pt. 1)

- __Sampling__ __bias__: GenAI knows _only_ what it has been _trained_ on + the pious hope that it learns to _generalize_

- Learning uses data taken __from the Web__ + possible provider-owned __company data__
    + there is documented use of previous users' _interactions_ as _feedback_ for subsequent training

{{% fragment %}}
##

> - __Niche__ information may <u>not</u> be learned correctly (or at all)
> - It is essential to __avoid sharing__ _sensitive_, _confidential_, or _copyrighted_ information
{{% /fragment %}}

---

## GenAI _learning_ cycle — __Consequences__ (pt. 2)

- Learning cycles are extremely __expensive__ in terms of _money_ and _computational resources_...

- ... performed __periodically__ (weeks? months?) to improve the _quality_ of the service
    + the _as-a-Service_ consumption model gives the user transparent access to the _updated_ service


{{% fragment %}}
##

> - __Recent__ information may <u>not</u> have been _learned_ yet
> - There is a risk of receiving __outdated__ or _incomplete_ answers from GenAI
> - GenAI gives the _impression_ of learning __during the conversation__, but it actually does so _offline_
{{% /fragment %}}

---

## Some technological solutions let you _choose_ (pt. 1)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-1.png" width="100%" max-h="50vh" >}}

---

## Some technological solutions let you _choose_ (pt. 2)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-2.png" width="100%" max-h="50vh" >}}

---

## Some technological solutions let you _choose_ (pt. 3)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-3.png" width="100%" max-h="50vh" >}}

---

## Some technological solutions let you _choose_ (pt. 4)

{{< image src="./logo-chatgpt.svg" height="2em" >}}
<br/>
{{< image src="./chatgpt-settings/no-learn-4.png" width="100%"  max-h="50vh" >}}

{{% /section %}}

---

{{< slide id="interfaces" >}}

# Main __technological__ solutions

## Categorized by type of __interface__

- _Conversational_: e.g. [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/login?returnTo=%2F%3F), [Scite](https://scite.ai)
- _Auto-completion_: e.g. [GitHub Copilot](https://github.com/features/copilot)
- _Programmatic_: e.g. [OpenAI Platform](https://openai.com/api/), [Hugging Face](https://huggingface.co/)
- _In-App_: e.g. [Microsoft 365 Copilot](https://www.microsoft.com/it-it/microsoft-365/copilot?market=it)
- _Audio/video editing_: e.g. [Suno](https://suno.com/), [Runway](https://runwayml.com/)
- _Inspection of generated material_: e.g. [GPTZero](https://gptzero.me/), [ZeroGPT](https://www.zerogpt.com/)

{{% color "red" %}}Non-exhaustive list!{{% /color %}}

---

## __Conversational__ interface

{{% multicol %}}
{{% col %}}
{{< image src="./logo-chatgpt.svg" height="2em" >}}
{{< image src="./interface-conversational.png" width="100%" link="https://chatgpt.com/share/6798dd04-8a98-8008-a751-bc374318bd9e" >}}
{{% /col %}}
{{% col %}}
<br>

- _Textual_ interaction that mimics a (__chat__) _exchange_
    + the user asks, the AI responds _reactively_
- The interface allows entering a __prompt__
    + optionally including _attachments_ (e.g. images, documents)
- Responses are __contextual__
    + i.e., the conversation _history_ affects _future_ responses
- The response contains __text__ (often _formatted_)
    + optionally: _images_, URLs, code

{{% fragment %}}

### Sometimes...

- ... before responding, the AI performs a __Web__ _search_
- important for obtaining _up-to-date_ results

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## __Auto-completion__ interface

{{% multicol %}}
{{% col %}}
{{< image src="./logo-copilot.svg" height="2em" >}}
{{< image src="./interface-autocompletion.gif" width="100%" >}}
{{% /col %}}
{{% col %}}
<br>

- The AI _suggests_ a __completion__ for the entered text
    + e.g., code, text, URLs
- The user __accepts__ (even partially) or _ignores_ the suggestion
- Used especially for __programming__ _code_

{{% fragment %}}

### Attention...
- ... __subscription__ pricing model (see [here](https://github.com/features/copilot/plans))
- ... potential __leaks__ of _sensitive_ information
- ... non-negligible __lock-in__ risk

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## __Programmatic__ interface

{{% multicol %}}
{{% col class="col-6" %}}
{{< image src="./logo-openai.svg" height="2em" >}}
```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="sk-1234567890abcdef1234567890abcdef")

async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            dict(role="user",
                 content="European countries, one by line")
        ],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end=", ")

asyncio.run(main())
```

Output:
```plaintext
Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Vatican City (Holy See),
```
{{% /col %}}
{{% col %}}

- __Programming language__ interacting with AI
    + e.g., _Python_, JavaScript

- The interaction remains of the _request-response_ type
    + the __program__ sends a _request_, the AI _responds_

{{% fragment %}}

### Enables

- __Parametric__ prompts, responses processed _automatically_
    + e.g. `list of LOCALITIES in AREA, one by line`
        + where `LOCALITIES` $\in$ {`cities`, `regions`, `states`}
        + and `AREA` $\in$ {`Europe`, `Asia`, `Africa`, `America`, `Oceania`}
        + results _sorted alphabetically_

- Writing __software__ that uses AI as a __service__
    + useful in both _industry_ and _research_

{{% /fragment %}}

{{% fragment %}}

### Attention...
- ... __usage-based__ pricing model (see [here](https://openai.com/api/pricing/))
    + proportional to the number of processed _tokens_
    + prices vary _by model_

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## __In-app__ interface

{{% multicol %}}
{{% col %}}
{{< image src="./logo-copilot-office.svg" height="2em" >}}
{{< image src="./interface-inapp.gif" width="100%" >}}
{{% /col %}}
{{% col %}}
<br>

- GenAI integrated into __desktop__ or _web_ __applications__
    + e.g., _Microsoft Office_ (Word, Excel, Outlook)

- support for an internal __conversational__ interface
    + a conversation that is intrinsically _contextualized_

- AI __automates__ _complex operations_ (within the app)
    + e.g., draft _writing_
    + e.g., _generation_ of formulas, charts

{{% fragment %}}

### Attention...
- ... __subscription__ pricing model (see [here](https://www.microsoft.com/it-it/microsoft-365/copilot?market=it#plans))
- ... potential __leaks__ of _sensitive_ information
- ... non-negligible __lock-in__ risk

{{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## Interface for __editing__ audio/video content (e.g. _music_)

{{% multicol %}}
{{% col %}}
{{< image src="./logo-suno.svg" height="2em" >}}
{{< image src="./generate-song-1.png" width="100%" >}}
{{% /col %}}
{{% col %}}
- __One-shot__ interaction to generate content
    + _input_: textual description of the content
    + _output_: content

- The interface then allows
    + _playback_ of the content
    + __editing__ of the content
        + e.g., _cutting_ parts, _changing_ key

{{% fragment %}}

### Example

- ["Song of Bacchus" (Lorenzo de' Medici, 1490)](https://it.wikipedia.org/wiki/Il_trionfo_di_Bacco_e_Arianna_(poesia)), rock
    + <https://suno.com/song/cce33ee7-a581-47ae-b9d1-806902e88e47>

{{% /fragment %}}
{{% /col %}}
{{% /multicol %}}

---

{{< slide id="modes" >}}

# Main __usage modes__

## Categorized by GenAI __role__

### GenAI as...

* ... a _search engine_: user is __searching for__ information
* ... a _(re)writing_ assistant: user is __writing__ documents
* ... a reading assistant: user is __extracting information__ from documents
* ... a data-processing assistant: user is __processing__ data
* ... a content generator: user is __creating__ content

{{% color "red" %}}Non-exhaustive list!{{% /color %}}

---

{{% import path="reusable/back.md" %}}
