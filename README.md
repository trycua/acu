<div align="center">
<h1>
  <div class="image-wrapper" style="display: inline-block;">
    <img src="img/logo.png" alt="logo" height="100" style="display: block; margin: auto;">
  </div>
  
  [![X Community](https://img.shields.io/badge/Community-black?logo=x&style=flat-square)](https://x.com/i/communities/1874549355442802764)
  
  ACU - Awesome Agents for Computer Use
</h1>
</div>

> An AI Agent for Computer Use is an autonomous program that can **reason** about tasks, **plan** sequences of actions, and **act** within the domain of a computer or mobile device in the form of clicks, keystrokes, other computer events, command-line operations and internal/external API calls. These agents combine perception, decision-making, and control capabilities to interact with digital interfaces and accomplish user-specified goals independently.

A curated list of resources about AI agents for Computer Use, including research papers, projects, frameworks, and tools.

## Table of Contents

- [ACU - Awesome Agents for Computer Use](#acu---awesome-agents-for-computer-use)
  - [Table of Contents](#table-of-contents)
  - [Articles](#articles)
  - [Papers](#papers)
    - [Surveys](#surveys)
    - [Frameworks & Models](#frameworks--models)
    - [UI Grounding](#ui-grounding)
    - [Dataset](#dataset)
    - [Benchmark](#benchmark)
    - [Safety](#safety)
  - [Projects](#projects)
    - [Open Source](#open-source)
      - [Frameworks & Models](#frameworks--models-1)
      - [Environment & Sandbox](#environment--sandbox)
      - [Automation](#automation)
    - [Commercial](#commercial)
      - [Frameworks & Models](#frameworks--models-2)
  - [Contributing](#contributing)

## Articles
- [Anthropic | Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku](https://www.anthropic.com/news/3-5-models-and-computer-use)
- [Bill Gates | AI is about to completely change how you use computers](https://www.gatesnotes.com/AI-agents)
- [Ethan Mollick | When you give a Claude a mouse](https://www.oneusefulthing.org/p/when-you-give-a-claude-a-mouse)
- [OpenAI | Introducing Operator: A research preview of an agent that can use its own browser to perform tasks for you](https://openai.com/index/introducing-operator)

## Papers

<details open>
<summary><b>Surveys</b></summary>

### Surveys

- [AI Agents for Computer Use: A Review of Instruction-based Computer Control, GUI Automation, and Operator Assistants](https://arxiv.org/abs/2501.16150) (Jan. 2025)
  - Comprehensive review establishing taxonomy of computer control agents (CCAs) from environment, interaction, and agent perspectives, analyzing 86 CCAs and 33 datasets

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) (Dec. 2024)
  - General survey of GUI agents

- [Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279) (Nov. 2024)
  - Focus on LLM-based approaches
  - [Website](https://vyokky.github.io/LLM-Brained-GUI-Agents-Survey/)

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) (Nov. 2024)
  - Comprehensive overview of foundation model-based GUI agents
  
<br/>
</details>

<details open>
<summary><b>Frameworks & Models</b></summary>

### Frameworks & Models

- [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) (Feb. 2025)
  - Novel RL approach (LOOP) for training IDAs directly in target environments
  - 32B parameter agent outperforms OpenAI o1 by 9 percentage points on AppWorld

- [Large Action Models: From Inception to Implementation](https://arxiv.org/abs/2412.10047) (Dec. 2024)
  - Comprehensive framework for developing LAMs that can perform real-world actions beyond language generation
  - Details key stages including data collection, model training, environment integration, grounding and evaluation

- [Guiding VLM Agents with Process Rewards at Inference Time for GUI Navigation](https://openreview.net/forum?id=jR6YMxVG9i) (Dec. 2024)
  - Novel reward-guided navigation approach

- [SpiritSight Agent: Advanced GUI Agent with One Look](https://openreview.net/forum?id=jY2ow7jRdZ) (Dec. 2024)
  - Single-shot GUI interaction approach

- [AutoGUI: Scaling GUI Grounding with Automatic Functionality Annotations from LLMs](https://openreview.net/forum?id=wl4c9jvcyY) (Dec. 2024)
  - Novel approach for automatic GUI functionality annotation

- [Simulate Before Act: Model-Based Planning for Web Agents](https://openreview.net/forum?id=JDa5RiTIC7) (Dec. 2024)
  - Novel model-based planning approach using LLM world models

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://arxiv.org/abs/2412.13194) (Dec. 2024)
  - Novel autonomous skill discovery framework for web agents
  - [Code](https://yanqval.github.io/PAE/)

- [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://openreview.net/forum?id=3Gzz7ZQLiz) (Dec. 2024)
  - Novel framework for contextualizing web pages to enhance LLM agent decision making

- [Digi-Q: Transforming VLMs to Device-Control Agents via Value-Based Offline RL](https://openreview.net/forum?id=CjfQssZtAb) (Dec. 2024)
  - Novel value-based offline RL approach for training VLM device-control agents

- [Magentic-One](https://www.microsoft.com/en-us/research/uploads/prod/2024/11/MagenticOne.pdf) (Nov. 2024)
  - Multi-agent system with orchestrator-led coordination
  - Strong performance on GAIA, WebArena, and AssistantBench

- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) (Sep. 2024)
  - Novel workflow memory framework for agents
  - [Code](https://github.com/zorazrw/agent-workflow-memory)

- [The Impact of Element Ordering on LM Agent Performance](https://arxiv.org/abs/2409.12089) (Sep. 2024)
  - Novel study on element ordering's impact on agent performance
  - [Code](https://github.com/waynchi/gui-agent)

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199) (Aug. 2024)
  - Novel reasoning and learning framework
  - [Website](https://www.multion.ai/blog/introducing-agent-q-research-breakthrough-for-the-next-generation-of-ai-agents-with-planning-and-self-healing-capabilities)

- [OpenWebAgent: An Open Toolkit to Enable Web Agents on Large Language Models](https://aclanthology.org/2024.acl-demos.8/) (Aug. 2024)
  - Open platform for web-based agent deployment
  - [Code](https://github.com/boxworld18/OpenWebAgent)

- [Agent-e: From autonomous web navigation to foundational design principles in agentic systems](https://arxiv.org/abs/2407.13032) (Jul. 2024)
  - Hierarchical architecture with flexible DOM distillation
  - Novel denoising method for web navigation

- [Apple Intelligence Foundation Language Models](https://arxiv.org/pdf/2407.21075) (Jul. 2024)
  - Vision-Language Model with Private Cloud Compute
  - Novel foundation model architecture

- [Tree search for language model agents](https://arxiv.org/abs/2407.01476) (Jul. 2024)
  - Multi-step reasoning and planning with best-first tree search
  - Novel approach for LLM-based agents

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://arxiv.org/abs/2406.11896) (Jun. 2024)
  - Novel reinforcement learning approach
  - [Code](https://github.com/DigiRL-agent/digirl)

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://arxiv.org/abs/2406.01014) (Jun. 2024)
  - Multi-agent collaboration for mobile device operation
  - [Code](https://github.com/X-PLUG/MobileAgent)

- [Octopus Series: On-device Language Models for Computer Control](https://arxiv.org/abs/2404.01549) (Apr. 2024)
  - v4: Graph of language models with functional tokens integration (Apr. 2024)
  - v3: Sub-billion parameter multimodal model for edge devices (Apr. 2024)
  - v2: Super agent for Android and iOS (Apr. 2024)
  - v1: Function calling of software APIs (Apr. 2024)
  - [Website](https://www.nexa4ai.com/octopus-v3)
  - [Code](https://github.com/NexaAI/octopus-v4)

- [AutoWebGLM: Bootstrap and reinforce a large language model-based web navigating agent](https://arxiv.org/abs/2404.03648) (Apr. 2024)
  - Novel approach for real-world web navigation and bilingual benchmark
  - [Code](https://github.com/THUDM/WebGLM)

- [Cradle: Empowering Foundation Agents towards General Computer Control](https://arxiv.org/abs/2403.03186) (Mar. 2024)
  - Focus on general computer control using Red Dead Redemption II as a case study
  - [Code](https://github.com/BAAI-Agents/Cradle)

- [Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://arxiv.org/abs/2403.02713) (Mar. 2024)
  - Novel Chain-of-Action-Thought framework for Android interaction
  - [Code](https://github.com/IMNearth/CoAT)

- [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945) (Feb. 2024)
  - Vision-language model for computer control
  - [Code](https://github.com/niuzaisheng/ScreenAgent)

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456) (Feb. 2024)
  - Vision-Language Model for PC interaction
  - [Code](https://github.com/OS-Copilot/OS-Copilot)

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://arxiv.org/abs/2402.07939) (Feb. 2024)
  - Specialized for Windows OS interaction
  - [Code](https://github.com/microsoft/UFO)

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://arxiv.org/abs/2402.11941) (Feb. 2024)
  - Novel comprehensive environment perception (CEP) approach for exhaustive GUI perception
  - Introduces conditional action prediction (CAP) for reliable action response

- [Intention-inInteraction (IN3): Tell Me More!](https://arxiv.org/abs/2402.09205) (Feb. 2024)
  - Novel benchmark for evaluating user intention understanding in agent designs
  - Introduces model experts for robust user-agent interaction

- [Dual-view visual contextualization for web navigation](https://arxiv.org/abs/2402.04476) (Feb. 2024)
  - Novel approach for automatic web navigation with language instructions
  - Key: HTML elements, visual contextualization

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615) (Feb. 2024)
  - Specialized for mobile UI and infographics understanding
  - Novel approach for visual interface comprehension

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) (Jan. 2024)
  - Demonstrates GPT-4V capabilities for web interaction
  - [Code](https://github.com/OSU-NLP-Group/SeeAct)

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158) (Jan. 2024)
  - Visual perception for mobile device interaction
  - [Code](https://github.com/X-PLUG/MobileAgent)

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) (Jan. 2024)
  - End-to-end approach for web interaction
  - [Code](https://github.com/MinorJerry/WebVoyager)

- [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914) (Dec. 2023)
  - Works across PC and Android platforms
  - [Code](https://github.com/THUDM/CogVLM)

- [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) (Dec. 2023)
  - Focused on smartphone interaction
  - [Code](https://github.com/mnotgod96/AppAgent)

- [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172) (Sep. 2023)
  - Novel approach to web navigation
  - [Code](https://github.com/Mayer123/LASER)

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231) (May 2021)
  - Reinforcement learning platform for Android interaction
  - [Code](https://github.com/google-deepmind/android_env)

<br/>
</details>

<details open>
<summary><b>UI Grounding</b></summary>

### UI Grounding

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/pdf/2408.00203) (Aug. 2024)
  - Novel vision-based screen parsing method for UI screenshots
  - Combines finetuned interactable icon detection and functional description models
  - [Code](https://github.com/microsoft/OmniParser)

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2404.05719) (Apr. 2024)
  - Mobile UI understanding
  - [Code](https://github.com/apple/ml-ferret)

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) (Jan. 2024)
  - Advanced visual grounding techniques
  - [Code](https://github.com/njucckevin/SeeClick)

- [Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://arxiv.org/abs/2410.18967) (Oct. 2024)
  - Multimodal LLM for universal UI understanding across diverse platforms
  - Introduces adaptive gridding for high-resolution perception
  - Preprint

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243) (Oct. 2024)
  - Universal approach to GUI interaction
  - [Code](https://github.com/OSU-NLP-Group/UGround)

- [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218) (Oct. 2024)
  - Comprehensive action modeling
  - [Code](https://github.com/OS-Copilot/OS-Atlas)

- [UI-Pro: A Hidden Recipe for Building Vision-Language Models for GUI Grounding](https://openreview.net/forum?id=5wmAfwDBoi) (Dec. 2024)
  - Novel framework for building VLMs with strong UI element grounding capabilities

- [Grounding Multimodal Large Language Model in GUI World](https://openreview.net/forum?id=M9iky9Ruhx) (Dec. 2024)
  - Novel GUI grounding framework with automated data collection engine and lightweight grounding module

<br/>
</details>

<details open>
<summary><b>Dataset</b></summary>

### Dataset

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents] (https://arxiv.org/pdf/2502.11357) (Feb. 2025)
  - Scalable multi-agent pipeline that leverages exploration for diverse web agent trajectory synthesis.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://arxiv.org/abs/2412.19723) (Dec. 2024)
  - Novel interaction-driven approach for automated GUI trajectory synthesis
  - Introduces reverse task synthesis and trajectory reward model
  - [Code](https://github.com/OS-Copilot/OS-Genesis)

- [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605) (Dec. 2024)
  - Web tutorial-based trajectory synthesis

- [ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights](https://arxiv.org/abs/2406.14596) (Jun. 2024)
  - Novel approach to continual learning from trajectories

- [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://arxiv.org/abs/2409.15637) (Sep. 2024)
  - Scalable demonstration generation

- [Multi-Turn Mind2Web: On the Multi-turn Instruction Following](https://arxiv.org/pdf/2402.15057) (Feb. 2024)
  - Multi-turn instruction dataset for web agents
  - [Code](https://github.com/magicgh/self-map)

- [CToolEval: A Chinese Benchmark for LLM-Powered Agent Evaluation](https://aclanthology.org/2024.findings-acl.928/) (Aug. 2024)
  - Chinese benchmark for agent evaluation
  - [Code](https://github.com/tjunlp-lab/CToolEval)

- [AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks](https://arxiv.org/abs/2407.15711) (Jul. 2024)
  - Benchmark for realistic and time-consuming web tasks
  - [Code](https://assistantbench.github.io)

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) (Jun. 2023)
  - Large-scale web interaction dataset
  - [Code](https://github.com/OSU-NLP-Group/Mind2Web)

- [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) (Jul. 2023)
  - Large-scale dataset for Android interaction
  - Real-world device control scenarios

- [WebShop: Towards Scalable Real-World Web Interaction](https://arxiv.org/abs/2207.01206) (Jul. 2022)
  - Dataset for grounded language agents in web interaction
  - [Code](https://github.com/princeton-nlp/WebShop)

- [Rico: A Mobile App Dataset for Building Data-Driven Design Applications](https://dl.acm.org/doi/10.1145/3126594.3126651) (Oct. 2017)
  - Mobile app UI dataset
  - Design-focused data collection

<br/>
</details>

<details open>
<summary><b>Benchmark</b></summary>

### Benchmark

- [A3: Android Agent Arena for Mobile GUI Agents](https://arxiv.org/abs/2501.01149) (Jan. 2025)
  - Novel evaluation platform with 201 tasks across 21 widely used third-party apps
  - [Website](https://yuxiangchai.github.io/Android-Agent-Arena/)
  - [Code](https://github.com/AndroidArenaAgent/AndroidArena)

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) (Apr. 2024)
  - Comprehensive evaluation framework
  - [Code](https://github.com/xlang-ai/OSWorld)

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) (May. 2024)
  - Android-focused evaluation
  - [Code](https://github.com/google-research/android_world)

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://arxiv.org/abs/2407.10956) (Jul. 2024)
  - Evaluation in data science workflows
  - [Code](https://github.com/xlang-ai/Spider2-V)

- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) (Jul. 2024)
  - Comprehensive benchmark with 750 natural tasks across 9 day-to-day apps and 457 APIs
  - GPT-4o achieves only ~49% on normal tasks and ~30% on challenge tasks
  - [Code](https://github.com/stonybrooknlp/appworld/)

- [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) (Jun. 2024)
  - Novel benchmark for evaluating agent-user interaction and policy compliance
  - State-of-the-art agents achieve <50% success rate and <25% consistency (pass^8)
  - [Code](https://github.com/sierra-research/tau-bench)

- [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://arxiv.org/abs/2406.08184) (Jun. 2024)
  - Mobile agent evaluation
  - [Code](https://github.com/MobileAgentBench/mobile-agent-bench)

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) (Jan. 2024)
  - Web-focused evaluation
  - [Code](https://github.com/web-arena-x/visualwebarena)

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://arxiv.org/abs/2409.08264) (Sep. 2024)
  - Windows OS-focused evaluation framework
  - [Code](https://github.com/microsoft/WindowsAgentArena)
  - [Website](https://microsoft.github.io/WindowsAgentArena/)

- [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144) (May. 2023)
  - Mobile-focused evaluation framework
  - [Code](https://github.com/X-LANCE/Mobile-Env)

<br/>
</details>

<details open>
<summary><b>Safety</b></summary>

### Safety

- [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) (Nov. 2024)
  - Security analysis of computer agents
  - [Code](https://github.com/SALT-NLP/PopupAttack)

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295) (Sep. 2024)
  - Privacy and security analysis

- [GuardAgent: Safeguard LLM Agent by a Guard Agent via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2406.09187) (Jun. 2024)
  - Safety mechanisms for agents

<br/>
</details>

## Projects

### Open Source

<details open>
<summary><b>Frameworks & Models</b></summary>

### Frameworks & Models

- [AutoGen](https://github.com/microsoft/autogen)
  - Framework for building AI agent systems.
  - It simplifies the creation of event-driven, distributed, scalable, and resilient agentic applications.

- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)  
  - Autonomous GPT-4 agent  
  - Task automation focus

- [Browser Use](https://github.com/browser-use/browser-use)  
  - Make websites accessible for AI agents with vision + HTML extraction  
  - Supports multi-tab management and custom actions with LangChain integration  

- [Claude Computer Use Demo](https://github.com/PallavAg/claude-computer-use-macos)  
  - MacOS implementation  
  - Claude integration  

- [Claude Minecraft Use](https://github.com/ObservedObserver/claude-minecraft-use)  
  - Game automation  
  - Specialized use case  

- [Computer Use OOTB](https://github.com/showlab/computer_use_ootb)  
  - Ready-to-use implementation  
  - Comprehensive toolset  

- [Cua](https://github.com/trycua)
  - Computer Use Interface & Agent

- [Cybergod](https://github.com/james4ever0/agi_computer_control)  
  - Advanced computer control  

- [Grunty](https://github.com/suitedaces/computer-agent)  
  - Computer control agent  
  - Task automation focus

- [Inferable](https://github.com/inferablehq/inferable)  
  - Distributed agent builder platform  
  - Build tools with existing code  

- [LaVague](https://github.com/lavague-ai/LaVague)  
  - AI web agent framework  
  - Modular architecture  

- [Mac Computer Use](https://github.com/deedy/mac_computer_use)  
  - MacOS-specific tools  
  - Anthropic integration  

- [NatBot](https://github.com/nat/natbot)  
  - Browser automation  
  - GPT-4 Vision integration  

- [OpenAdapt](https://github.com/OpenAdaptAI/OpenAdapt)  
  - AI-First Process Automation  
  - Multimodal model integration  

- [OpenInterface](https://github.com/AmberSahdev/Open-Interface/)  
  - Open-source UI interaction framework  
  - Cross-platform support  

- [OpenInterpreter](https://github.com/OpenInterpreter/open-interpreter)  
  - General-purpose computer control framework  
  - Python-based, extensible architecture  

- [Open Source Computer Use by E2B](https://github.com/e2b-dev/secure-computer-use/tree/os-computer-use)  
  - Open-source implementation of computer control capabilities  
  - Secure sandboxed environment for AI agents  

- [Self-Operating Computer](https://github.com/OthersideAI/self-operating-computer) (Nov. 2023) 
  - The first Computer Use framework created
  - Computer control framework  
  - Vision-based automation

- [Skyvern](https://github.com/skyvern-ai/skyvern)  
  - AI web agent framework
  - Automate browser-based workflows with LLMs using vision and HTML extraction

- [Surfkit](https://github.com/agentsea/surfkit)  
  - Device operation toolkit  
  - Extensible agent framework  

- [WebMarker](https://github.com/reidbarber/webmarker)  
  - Web page annotation tool  
  - Vision-language model support  

<br/>
</details>

<details open>
<summary><b>UI Grounding</b></summary>

### UI Grounding

- [AskUI/PTA-1](https://huggingface.co/AskUI/PTA-1)
  - A small vision language model for computer & phone automation, based on Florence-2.
  - With only 270M parameters it outperforms much larger models in GUI text and element localization. 

- [Microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser)
  - A general screen parsing tool, which interprets/converts UI screenshot to structured format, to improve existing LLM based UI agent

<br/>
</details>

<details open>
<summary><b>Environment & Sandbox</b></summary>

### Environment & Sandbox

- [Cua](https://github.com/trycua)
  - macOS/Linux Sandbox on Apple Silicon

- [dockur/windows](https://github.com/dockur/windows)
  - Windows inside a Docker container

- [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop)
  - Secure desktop environment
  - Agent testing platform

- [qemus/qemu-docker](https://github.com/qemus/qemu-docker)
  - Docker container for running virtual machines using QEMU

<br/>
</details>

<details open>
<summary><b>Automation</b></summary>

### Automation
- [nut.js](https://github.com/nut-tree/nut.js)
  - Native UI automation
  - JavaScript/TypeScript implementation

- [PyAutoGUI](https://github.com/asweigart/pyautogui)
  - Cross-platform GUI automation
  - Python-based control library

<br/>
</details>

### Commercial

<details open>
<summary><b>Frameworks & Models</b></summary>

### Frameworks & Models

- [Anthropic Claude Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use)
  - Commercial computer control capability
  - Integrated with Claude 3.5 models

- [Multion](https://www.multion.ai)
  - AI agents that can fully complete tasks in any web environment.

- [Runner H](https://www.hcompany.ai/)
  - Advanced AI agent for real-world applications.
  - Scores 67% on WebVoyager

<br/>
</details>

## Contributing

We welcome and encourage contributions from the community! Here's how you can help:

- **Add new resources**: Found a relevant paper, project, or tool? Submit a PR to add it
- **Fix errors**: Help us correct any mistakes in existing entries
- **Improve organization**: Suggest better ways to structure the information
- **Update content**: Keep entries up-to-date with latest developments

To contribute:
1. Fork the repository
2. Create a new branch for your changes
3. Submit a pull request with a clear description of your additions/changes
4. Post in the [X Community](https://x.com/i/communities/1874549355442802764) to let everyone know about the new resource

For an example of how to format your contribution, please refer to [this PR](https://github.com/francedot/acu/pull/1).

<br/>

*Thank you for helping spread knowledge about AI agents for computer use!*
