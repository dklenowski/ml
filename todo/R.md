Categories: software
Tags: R
      regression
      plot

## R Stuff

### Load CSV Data

    tbl<-read.csv('<path>', header=FALSE)

- A `table` is synonymous with `data frame`
- To set the column names:

    colnames(tbl) <- c("col1", "col2")
    
### View data

    View(tbl)

### Scatterplot Data

    plot(tbl)

### Regression

    x<-lm(V1~V2, data=tbl)

- where:
  - `V1` and `V2` are the variable names (equate to `y` and `x` respectively).
  - `tbl` is the CSV data

#### Display regression details

- e.g. Residuals, Coefficients, R-Squared

        summary(x)

#### Plotting Regression Details

- e.g. Residuals, Q-Q plot etc.

        plot(x)

- To plot a particular graph:

        plot(m,which=1)

#### Add a regression line to a scatterplot

    x<-lm(V1~V2,data=tbl)
    plot(tbl)
    abline(x)

### Matrices

- To load the matrix

        A = matrix( c(0, 1, -2, 1, 0, 1, -2, 1, 0), nrow=3, ncol=3)
        x = matrix( c(0, 0, 0), nrow=3, ncol=1)

### Solving 

- To solve for `x` in `b=Ax`


        A = matrix( c(0, 1, -2, 1, 0, 1, -2, 1, 0), nrow=3, ncol=3)
        b = matrix( c(-1, -1, 1), nrow=3, ncol=1)
        solve(A, b)
