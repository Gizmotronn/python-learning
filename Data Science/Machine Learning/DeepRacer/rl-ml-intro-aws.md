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

### Reward function - examples

**All wheels on track; distance from center, trackwidth**

```python
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return float(reward)
```

**Follow center line -- track_width; distance from center**

```python
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)
```

**No incentive - constant reward on each step**

```python
def reward_function(params):
    '''
    Example of no incentive
    '''

    # Always return 1 if the car does not crash
    return 1.0
```

#### The Reward Function

**1. Stay on Track**

* In this script, a high reward is given when the car stays on the track
* "Points" are penalized if the car deviates from the track boundaries

The function uses the following parameters:

* all_wheels_on_track
* distance_from_center
* track_width

These parameters determine if the car is on the track, and therefore can give a high reward if so

As the function doesn't reward any other kind of behavior, it can take a longer time to converge to a specific behavior

*Script*:

```python
def reward_function(params):
    # Example of rewarding the agent if it stays inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    # By Default, the function returns a low reward
    reward = 1e-3
    
    # If no wheels go off the track and the agent is between the track borders, a high reward is given
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
        
    # Always return a float value
    return float(reward)
```

