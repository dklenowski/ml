Categories: algorithms
Tags: algorithm
      markov
      memory
      variable
      
## Reference ##

- Sequence memory for prediction, inference and behaviour, Jeff Hawkins.

## Notes ##

- Representations of sequences are passed up the hierarchy, forming elements of sequences in upper regions.
- Also, predictions of next elements in sequence are passed down the hierarchy.

### Auto Associative Recall ###

- As inputs arrive, memory has to decide which learned sequences best match the input.
  - Must be able to recognise sequences even if it is presented with a partial sequence from the middle of the previously learned sequence.

### Variable Order Memory ###

- Uses variable order markov model.

        $latex P(X_{t+1}|X_{t},X_{t-1},...X_{0})=P(X_{t+1}|X_{t}) $

- where: $latex X_{t} $ is the input at time $latex t $.
- e.g. fourth order

        $latex P(X_{t+1}|X_{t},X_{t-1},X_{t-2},..X_{o})=P(X_{t+1}|X_{t},X_{t-1},X_{t-2},X_{t-3}) $

### Biological Implications ###

- Do not assume individual cells are sufficient to represent anything.
- In crude way:
  - Downward flowing information represents expectation.
  - Upward flowing information represents reality.
- Since cell layers are learning feed forward sequences (layers 3 and 4) and other layers are learning feedback sequences (layers 2 and 6).
- Layer 5 is where they are combined to form a belief.


### State Splitting ###

- Used to store sequences

        A      D        A ---> C1 ---> D
          \   /\
          \/  /
            B  
          /\  \
          /   \/
        B      E        B ---> C2 ---> E


- **State** - Transition from input state (i) to (j).
- When 1 state participates in >1 sequence, state is split.

