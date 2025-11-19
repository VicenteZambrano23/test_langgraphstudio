# Langgraph Studio UI investigation

This repository has been established to facilitate the evaluation and analysis of the LangGraph Studio UI by the Cognizant Generative AI Spain Community. 
Additionally, it provides comprehensive documentation within this README to enable community members to rapidly deploy and test projects and proof-of-concepts (POCs) utilizing this interface. 
Furthermore, it documents the constraints and limitations associated with operating the User Interface under the free tier subscription model.

## Deployment Guide

To configure and deploy the UI, follow the steps outlined below:

1. Navigate to the LangSmith platform (https://docs.langchain.com/langsmith/create-account-api-key). Create a new project and generate an API key. Ensure authentication is performed within the EU region.

2. Configure the `.env` file according to the specifications provided in `.env.sample`. Retain the default values for `LANGSMITH_TRACING_V2` and `LANGSMITH_ENDPOINT` as defined in the sample configuration.

3. Execute the following commands for Windows environment setup:
    - `python3 -m venv .venv`
    - `.venv\Scripts\Activate.ps1`
    - `pip install -r requirements.txt`
    - `langgraph dev`

4. The `agent_system.py` file contains a reference implementation utilizing a dummy LangGraph system. It is recommended to validate the deployment using this placeholder configuration to mitigate potential integration issues. Subsequently, implement your custom agent system within this script and reinitialize the application.

**Technical Requirements:**
- Python version 3.11 or higher is required
- This configuration is optimized for Azure OpenAI endpoints. For alternative model providers, modify the corresponding environment variables (`AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `API_VERSION`, `MODEL_NAME`, `DEPLOYMENT_NAME`)

## Free Tier Constraints and Limitations

**Platform Restrictions:**
- Production deployment capabilities are unavailable under the free tier
- Monthly trace limit of 5,000 traces

**User Interface Constraints:**
- UI customization is not supported

## Application Use Cases

This tool provides significant value across the following scenarios:

- **Development and Testing**: Facilitates comprehensive debugging and validation of LangGraph agent systems during the development lifecycle
- **Client Communication**: Enables enhanced explainability and transparency of AI agent system behavior for stakeholder presentations and demonstrations
- **System Observability**: Delivers high-level observability and monitoring capabilities through a low-code/no-code implementation approach
- **Rapid Prototyping**: Accelerates deployment timelines for pre-defined agent system architectures
