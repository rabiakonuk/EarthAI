# System Architecture for EarthAI: Integrating Prithvi Model with AIRS Data

## Introduction

This document outlines the system architecture designed to optimize the processing of AIRS data and the execution of the Prithvi model, inspired by principles from the ORCA project. Our goal is to develop a distributed system that incorporates dynamic scheduling and selective batching to enhance efficiency and scalability.

## Overview of System Components

The EarthAI system architecture comprises several key components, each playing a critical role in processing AIRS data and serving the Prithvi model. Below is a high-level overview of these components:

- **Data Ingestion and Preprocessing**: Automates the downloading, conversion, and initial preprocessing of AIRS data.
- **Distributed Computing Infrastructure**: Utilizes cloud resources and containerization to scale processing and model serving.
- **Dynamic Task Scheduler**: Manages and prioritizes tasks based on system load and available resources.
- **Selective Batching Mechanism**: Groups data processing tasks intelligently to optimize throughput without compromising on processing quality.
- **Model Serving**: Facilitates the deployment and serving of the Prithvi model for inference tasks.

## High-Level Architecture Diagram

Here, you would include a diagram that visually represents the system architecture outlined above. Use an online tool like Lucidchart or Draw.io to create your diagram, then embed or link it here.


Ensure the diagram illustrates the flow of data through the system, interactions between components, and how distributed computing resources are orchestrated.

## Detailed Component Design

### Data Ingestion and Preprocessing

Detail the automated processes for downloading AIRS data, converting file formats, and preprocessing data to prepare it for analysis. Mention any specific tools or libraries used (e.g., `wget`, `h4toh5`, Pandas).

### Distributed Computing Infrastructure

Describe the setup for distributed computing, including the use of Kubernetes for orchestrating containerized applications and cloud services (e.g., AWS EC2, Google Cloud Compute) for hosting and scaling resources.

### Dynamic Task Scheduler

Explain the logic and technology behind the dynamic task scheduler, focusing on how it prioritizes tasks based on current demand and resource availability. Include considerations for iteration-level scheduling.

### Selective Batching Mechanism

Detail the selective batching mechanism, including how it decides which tasks to group together and the criteria used (e.g., data size, complexity). Discuss any challenges in implementing selective batching and how they were addressed.

### Model Serving

Outline the approach for serving the Prithvi model, including any modifications made to the model architecture for compatibility with AIRS data. Discuss how model serving is integrated with the distributed computing infrastructure.

## Technology Stack

Provide a list of the primary technologies and frameworks chosen for the project, explaining the rationale behind each choice:

- **PyTorch Distributed** for model training and inference, leveraging CUDA for GPU acceleration.
- **Apache Spark** for scalable data processing, deployed on Kubernetes for flexibility and scalability.
- **Kubernetes** for orchestrating the deployment of containerized applications.
- **Prometheus and Grafana** for monitoring system performance and health.
- **Elasticsearch, Logstash, and Kibana (ELK Stack)** for logging and debugging.

## Conclusion

Summarize the architecture's design goals, emphasizing how each component and chosen technology contributes to the project's overall objectives. Highlight any areas for future development or potential challenges in scaling the system.

