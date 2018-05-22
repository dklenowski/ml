Categories: overview 
Tags: statistics
      variance
      mean

## Concepts

### Mean

    $latex {Mean}\mathrm{{=}}\overline{X}\mathrm{{=}}\frac{\mathop{\sum}\limits_{}\limits^{n}{{x}_{i}}}{n} $

### Standard Deviation

- The variance typically provides a better measure of spread than the mean.

        $latex {S}\tan{dardDeviation}\mathrm{{=}}{s}\mathrm{{=}}\sqrt{\frac{\mathop{\sum}\limits_{\hspace{0.33em}}\limits^{n}{{\mathrm{(}}{x}_{i}\mathrm{{-}}\overline{X}{\mathrm{)}}^{2}}}{{\mathrm{(}}{n}\mathrm{{-}}{1}{\mathrm{)}}}} $

### Variance

        $latex {Variance}\mathrm{{=}}{s}^{2}\mathrm{{=}}{var}{\mathrm{(}}{X}{\mathrm{)}}\mathrm{{=}}\frac{\mathop{\sum}\limits_{\hspace{0.33em}}\limits^{n}{{\mathrm{(}}{x}_{i}\mathrm{{-}}\overline{X}{\mathrm{)}}^{2}}}{{\mathrm{(}}{n}\mathrm{{-}}{1}{\mathrm{)}}} $
        $latex s=\sqrt{s^{2}} $

- Note, if using the complete population, use *n* instead of *n-1*

### Covariance

- Measure of spread with respect to 2 dimensions

        $latex {cov}{\mathrm{(}}{X}{\mathrm{,}}{Y}{\mathrm{)}}\mathrm{{=}}\frac{\mathop{\sum}\limits_{\hspace{0.33em}}\limits^{n}{{\mathrm{(}}{x}_{i}\mathrm{{-}}\overline{X}{\mathrm{)(}}{y}_{i}\mathrm{{-}}\overline{Y}{\mathrm{)}}}}{{\mathrm{(}}{n}\mathrm{{-}}{1}{\mathrm{)}}} $

- Covariance follows multiplicative and communitative rules:

        $latex {cov}{\mathrm{(}}{X}{\mathrm{,}}\hspace{0.33em}{Y}{\mathrm{)}}\mathrm{{=}}{cov}{\mathrm{(}}{Y}{\mathrm{,}}{X}{\mathrm{)}} $

#### Analysis

$latex cov(X,Y) $ is positive - Both dimensions increase together.

$latex cov(X,Y) $ is negative - As one dimension increases, the other decreases.

$latex cov(X,Y)=0 $ - The dimensions are independent of each other (i.e. there is no trend).

### Covariance Matrix

- For n dimensions:

        $latex {NumberOfCovariances}\mathrm{{=}}\frac{n\mathrm{!}}{{\mathrm{(}}{n}\mathrm{{-}}{2}{\mathrm{)!}}^{2}} $

- The covariance matrix is defined as:

        $latex {C}^{nxn}\mathrm{{=}}{\mathrm{((}}{c}_{ij}{c}_{ij}{\mathrm{)}}\mathrm{{=}}{cov}{\mathrm{(}}{\dim}_{i}{\mathrm{,}}{\dim}_{j}{\mathrm{))}} $

- e.g. for 3 dimensions

        $latex C=\left[\begin{array}{ccc} cov(x,x) & cov(x,y) & cov(x,z)\\ cov(y,x) &cov(y,y) & cov(y,z)\\ cov(z,x) & cov(z,y) & cov(z,z)\end{array}\right] $

- Notes:
  * Main diagonal contains variances (i.e. single) for that dimension
  * Matrix is symmetrical about the main diagonal since cov(a,b)=cov(b,a)


## Probability ##

### Terms ###

#### $latex \cap $

- Intersection.
- *and*


#### $latex \cup $

- Union.
- *or*


### Discrete Conditional Probability

- Given a discrete sample space:

        $latex \Omega=\left\{ w_{1},w_{2},w_{3}..,w_{n}\right\}  $

- with distribution:

        $latex f_{n}=m(w_{j}) $

- where:

        $latex m(w_{j})\geqslant0 $
        $latex {\displaystyle \sum_{w\epsilon\Omega}m(w_{j})=1} $

- The probability of event *E* (consisting of multiple events $latex w\_{j} $).

        $latex P(E)={\displaystyle \sum_{w\epsilon E}m(w_{j})} $

- where the elementary event (i.e. the probability of a single event $latex w\_{j} $).

        $latex P(\left\{ w_{j}\right\} )=m(w_{j}) $

