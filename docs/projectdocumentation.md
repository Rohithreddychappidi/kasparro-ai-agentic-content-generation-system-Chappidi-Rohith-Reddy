
## Multi-Agent Content Generation System

---

## 1. Problem Statement

The objective is to design and implement a modular, agent-based automation system that can take a small product dataset and automatically generate three structured outputs:

1. A FAQ page
2. A Product Description page
3. A Comparison page

All outputs must be generated in clean, machine-readable JSON format.

The system must show:

* Collaboration between multiple agents
* Template-based content generation
* Reusable logic blocks
* A clear automation flow
* Proper agent boundaries
* A non-monolithic, well-structured design

This project reflects practical AI engineering practices focused on system-level thinking instead of simple prompting.

---

## 2. Solution Overview

This project implements a multi-agent content generation pipeline. The system reads raw product data, converts it into a standard internal format, and then passes it through specialised agents that generate questions, answers, structured pages, and comparisons.

The solution includes the following agents:

* Parser Agent
* Question Generator Agent
* FAQ Answer Agent (via logic block)
* Template Agent
* Comparison Agent
* Page Assembly Agent

Reusable logic blocks (benefits, usage, safety, comparison, FAQ answer) ensure modularity and extensibility. A central Orchestrator coordinates the complete workflow from input to JSON output. The final output files are:

* faq.json
* product_page.json
* comparison_page.json

---

## 3. Scope and Assumptions

### Scope

* Works with one product dataset at a time
* Automatically generates three JSON pages
* Uses only the data provided in the input
* Fully deterministic outputs
* Template-based content structure

### Assumptions

* The product dataset follows a similar structure for future inputs
* Fictional Product B can be created for comparison
* The system runs in a Python environment
* Agents communicate only through structured dictionaries and do not share global state

---

## 4. System Design

### 4.1 Architecture Summary

The system is designed using multiple agents, logic blocks, standardised templates, and a central orchestrator. Each component has a single responsibility.

Workflow:

```
Raw Product Data
       |
Parser Agent
       |
Clean Product Model
       |
Question Generator Agent
       |
Questions
       |
Template Agent + Logic Blocks
       |
FAQ Page + Product Page
       |
Comparison Agent
       |
Comparison Page
       |
Page Assembly Agent
       |
JSON Outputs
```

---

### 4.2 Agents

#### 1. ParserAgent

Converts raw product fields into a clean, consistent internal model used by other agents.

#### 2. QuestionGeneratorAgent

Generates 12–15 user-focused questions across informational, usage, safety, purchase and comparison categories.

#### 3. TemplateAgent

Applies the FAQ, product, and comparison templates.
Uses logic blocks to fill fields such as benefits, usage, safety and answers.

#### 4. ComparisonAgent

Compares Product A with a fictional Product B.
Finds ingredient overlap, price difference and benefit differences.

#### 5. PageAssemblyAgent

Saves the generated content as JSON files in the output folder.

---

### 4.3 Logic Blocks

Reusable logic blocks include:

* Benefits Block: creates structured benefit summaries
* Usage Block: generates usage instructions
* Safety Block: generates side effect and warning information
* Comparison Block: compares products
* FAQ Answer Block: generates realistic answers to user questions using only product data

---

### 4.4 Templates

The system uses simple JSON templates.

#### FAQ Template

```
{
  "faqs": []
}
```

#### Product Page Template

```
{
  "name": "",
  "ingredients": [],
  "benefits_block": {},
  "usage_block": {},
  "safety_block": {},
  "price": ""
}
```

#### Comparison Template

```
{
  "product_a": {},
  "product_b": {},
  "comparison": {}
}
```

---

### 4.5 Orchestrator

The Orchestrator controls the entire workflow:

1. Load the raw product dataset
2. Run the Parser Agent
3. Generate the questions
4. Use logic blocks to generate answers
5. Generate the FAQ and product pages
6. Generate the comparison page
7. Save all outputs as JSON

This creates a clean, predictable automation pipeline.

---

## 5. Output Structure

### faq.json

Contains a list of questions with automatically generated answers.
Answers are created using only the provided product information.

### product_page.json

Contains structured information about ingredients, benefits, usage, safety, and price.

### comparison_page.json

Contains Product A, Product B and a comparison section including price comparison, ingredient overlap and benefit differences.

---

## 6. Conclusion

This system meets all the requirements of the Kasparro Applied AI Engineer Challenge. It is modular, template-based, agent-driven and fully automated.

It demonstrates:

* Multi-agent architecture
* Template-driven content generation
* Use of reusable logic blocks
* Structured JSON output
* Clean system design principles

This project reflects the engineering expectations at Kasparro and showcases the ability to design and build practical AI-driven automation systems.

---

