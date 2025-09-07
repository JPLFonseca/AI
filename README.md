### AI for Autonomous Systems

This repository contains the project for a course on **Artificial Intelligence for Autonomous Systems**. The project explores and implements concepts related to artificial intelligence and software engineering to create an autonomous agent.

The report details the theoretical foundations and practical implementation of an autonomous agent designed to perceive its environment, process perceptions, and execute actions accordingly. The project leverages various programming constructs and design patterns to manage complexity and ensure a systematic, quantifiable approach to software development.

---

### Key Topics Covered

The report and the project's implementation delve into the following areas:

* **Intelligent Agents**: The report explores various agent architectures, including reactive and deliberative agents.
* **Reactive Agent Architecture**: This section discusses agents that behave based on stimulus-response relationships without explicit internal state representations. The architecture is defined by a perception-reaction-action cycle.
* **Deliberative Agent Architecture**: This architecture focuses on agents that use memory to preserve past situations and consider future outcomes to make decisions. This architecture introduces practical reasoning for goal-oriented planning.
* **Automatic Reasoning and Decision-Making**: The report describes how state-space search can be used to solve planning problems. It discusses various search algorithms, including depth-first, breadth-first, uniform-cost, and A\* search.
* **Reinforcement Learning**: This section explains an approach where an agent learns through interaction with its environment, receiving feedback in the form of rewards and penalties to improve its choices over time. The report mentions algorithms like SARSA and Q-Learning.

---

### Project Implementation

The project involved creating a game with an autonomous character. The character's behavior was controlled by a state machine that processed environmental events (e.g., silence, noise, animal) and triggered corresponding actions (e.g., search, approach, photograph).

The implementation highlights key software engineering principles:

* **Modularity**: The state machine was implemented generically so it could be reused in other projects.
* **Abstraction and Factorization**: These concepts were used to manage complexity by eliminating redundancy and creating models that simplify essential logic.
* **Reduced Coupling**: Interfaces, like the `Comportamento` (Behavior) class, were used to minimize dependencies between subsystems.

The code structure includes classes for states, operators, and search mechanisms. It defines a `MecanismoProcura` (SearchMechanism) as an abstract class for a generalized search mechanism and a `Fronteira` (Frontier) class that represents the exploration frontier. It also includes specific search implementations like `ProcuraProfundidade` (DepthFirstSearch).
