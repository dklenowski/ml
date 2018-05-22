Categories: logic
Tags: logic

### Reference ###

Artificial Intelligence, A modern Approach, 2nd Edition

### Atomic Sentences

- Indivisible syntactic elements.
- Consist of a single prepositional symbol.
  - Each symbol either `true` or `false`.

### Logical Connectives ###

#### $latex \neg $  ####

- Not.
- e.g. $latex \neg W\_{1,3} $ called negation of $latex W\_{1,3} $.

####  $latex \wedge $ ####

- And.
- Conjunction.
- A sentence whose main connective is $latex \wedge $.
- e.g. $latex W\_{1,3} \wedge P\_{3,1} $.

#### $latex \vee $ 

- Or.
- Disjunction.
- e.g. $latex W\_{1,3} \vee P\_{3,1} $.

####  $latex \Rightarrow $  ####

- Implies.
- Implication.
- e.g. $latex (W\_{1,3} \vee P\_{3,1}) \Rightarrow \neg W\_{2,2} $.
  - where:
      - $latex (W\_{1,3} \vee P\_{3,1}) $ - premise/antecedent
      - $latex \neg W\_{2,2} $ - conclusion/consequent.

#### $latex \Leftrightarrow $

- Biconditional.
- If and only if.
- e.g. $latex W\_{1,3} \Leftrightarrow W\_{2,2} $.

#### De Morgans Laws ####

        $latex \neg P \wedge \neg Q \equiv \neg (P \vee Q) $
        $latex \neg (P \wedge Q) \equiv \neg P \vee \neg Q $
        $latex P \wedge Q \equiv \neg (\neg P \vee \neg Q) $
        $latex P \vee Q \equiv \neg (\neg P \wedge \neg Q) $


### First Order Logic ###

#### Universal Quantification ($latex \forall $).

- For all.
- i.e. makes a statement about every object.
- e.g. $latex \forall\; x King(x) \Rightarrow Person(x) $.
  - which means "For all x, if x is a king then x is a person."
  - $latex x $ is called a variable.
  - Convention, variables lowercase.
  - A term with no variables called a ground term.

##### Notes

      $latex \forall\; P $ 

- Where $latex P $ is any logical expression, says that $latex P $ is true for every object $latex x $.
- More precisely, $latex \forall\; P $  is true in a given model under a given interpretation, where each extended interpretation specifies a domain element to which $latex x $ refers.

#### Existential Quantification ($latex \exists $).

- For some.
- i.e. make a statement about some object in the universe (without naming it).
- e.g. $latex \exists x\; Crown(x) \vee OnHead(x, John) $.
  - $latex \exists x $ is pronounced "There exists an x such that.." or "For some x.."
  - $latex \exists x\; P $ says that P is true for at least one object x.
  - $latex \exists x\; P $ is true in a given model under a given interpretation if P is true in at least one extended interpretation that assigns x to a domain element.

#### Nested Quantifiers ####

- e.g. "Brothers are siblings"

        $latex \forall x \forall y\; Brother(x, y) \Rightarrow Sibling(x, y) $

- e.g. to say that siblings is a symmetric relationship

        $latex \forall x,y\; Sibling(x, y) \Leftrightarrow Sibling(y, x) $

- e.g. "Everybody loves somebody"

        $latex \forall x \exists y\; Loves(x, y) $

- e.g. "There is someone who is loved by everyone"

        $latex \exists y\; \forall x\; Loves(x, y) $

    - i.e. order of quantification is important.

#### Connections between  $latex \forall $ and $latex \exists $ ####

- These quantifiers are connected through negation.

      $latex \forall x\; \neg Likes(x, Parsnips) $

  - is equivalent to:

      $latex \neg \exists x\; Likes(x, Parsnips) $

- e.g. "Everyone likes ice cream" implies there is no one who does not like ice cream.

      $latex \forall x\; Likes(x, IceCream) $

  - is equivalent to:

      $latex \neg \exists x\; \neg Likes(x, IceCream) $

- Since $latex \forall $ is a conjunction over universe of objects and $latex \exists $ is a disjunction, therefore observe De Morgan's rules
  - i.e.

          $latex \forall x\; \neg P \equiv \neg \exists x\; P $
          $latex \neg \forall x\; P \equiv \exists x\; \neg P $
          $latex \forall x\; P \equiv \neg \exists x\; \neg P $
          $latex \exists x\; P \equiv \neg \forall x\; \neg P $


