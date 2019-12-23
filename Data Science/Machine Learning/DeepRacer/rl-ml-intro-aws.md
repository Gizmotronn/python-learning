https://d2k9g1efyej86q.cloudfront.net/

# Introduction to Reinforcement Learning

## AWS DeepRacer Preview

* Reinforcement learning is a type of machine learning
* An *agent* explores an *environment* to **learn** how to **perform desired tasks** by taking *actions* with good outcomes and avoiding actions with bad outcomes
* A reinforcement learning model will *learn from its experiences* and will learn to *identify* which actions lead to the *best rewards*

Other types of machine learning include:

* Supervised: Example-driven training
  * Labeled data [sets] of known outputs for given inputs, a model is trained to predict output for new inputs
* Unsupervised learning: Interference-based training
  * With unlabeled data [sets] without known outputs, a model is trained to identify related structures or similar patterns within the input data.

**Reward?**

* In reinforcement learning, an *agent* interacts with an *environment* with an objective to maximize its total *reward*
* The agent takes an *action* based on the environment *state*, which then returns the reward and the next state.
* Using trial and error, the agent learns from this and after initially taking random actions, it starts identifying the actions that lead to long-term rewards



*Agent*

* The agent simulates the AWS DeepRacer vehicle in the simulation for training
* It embodies the neural network that controls the vehicle, taking inputs and deciding actions

*Environment*

* Contains a track that defines where the agent can go and what state it can be in
* The agent explores the environment to collect data to train the underlying neural network

*State*

* A state represents a snapshot of the environment the agent is in at a point in time
* For the DR, a state is an image captured by the front-facing camera on the vehicle

*Action*

* An action is a move made by the agent in the current state
* For the DR, an action corresponds to a move at a particular speed and steering angle

*Reward*

* The reward is the score given as feedback to the agent when it takes an action in a given state
* The reward is returned by a reward function - training
* You define/supply a reward function to specify what is actions are desirable for the agent to take in a given state



**Training RL Models**

* Training is an iterative process
* In the simulator, the agent explores the environment and builds up experience
* The experiences collected are used to update the neural network periodically, these then are used to create more experiences



**Reward function for Deep Racer**

* The reward function is a python function.
* It is given certain parameters that describe the current state; it then returns a numeric reward value
* These parameters include:
  * Position on track (x, y parameters)
  * Heading (orientation of the vehicle in degrees. Measured anticlockwise from the x-axis)
  * Waypoints (Ordered list of milestones placed along the track. Each waypoint is a pair of x,y coords)
  * Track width (width of the track in meters)
  * Distance from center line (measures the displacement of the vehicle from the center of the track)
    * is_left_of_center: boolean (true/false)
  * All wheels on track - boolean (true/false)
  * Speed - meters per second (numerical value)
  * Steering Angle - (negative if steering right - measured in degrees)