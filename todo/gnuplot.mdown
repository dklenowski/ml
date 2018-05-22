Categories: graphing
Tags: gnuplot
      regression
      graph

## GnuPlot

### Operators

- `**` - exponentiation e.g. x^2 = x**2
- `norm(x)` - Normal Gaussian distribution function

### Set Commands

    gnuplot> set title "<title>"
    gnuplot> set xlabel "<xlabel>"
    gnuplot> set ylabel "<ylabel>"
    gnuplot> set noyzeroaxis
    gnuplot> set noyzeroaxis
    gnuplot> set border
    gnuplot> set nogrid
    gnuplot> set nokey
    gnuplot> set autoscale     # let gnuplot determine ranges
    gnuplot> set logscale      # ploy using log axes
    gnuplot> set logscale <axis> # set logscale for a single (x, y) axis
    gnuplot> show logscale
    gnuplot> set nologscale
    gnuplot> set xtics ( 1, 2, 3)

- Notes:
  - Can use `\n` in title/labels

### Loading Data From File

- e.g. you have a file called “work.gnu”

        set time
        set title "File Graph"
        set hidden3d
        ....

- to load file

        gnuplot> load 'work.gnu'
        gnuplot> '~/work.gnu'
        ....
        gnuplot> save "work.gnu"          # save commands to file

- Change paths using

        gnuplot> pwd
        gnuplot> cd "~/gnuplot"

### Using Times

    gnuplot> set xdata time
    gnuplot> set timefmt "%d/%m/%Y %H:%M:%S"
    gnuplot> set data style linespoints

### Plotting

    gnuplot> plot "<datafile>" using 1:3     # plot using colums 1 and 3
                                             # NB Colums referenced from 1

#### Plotting Options

    gnuplot> set data style linespoints    # display data as points
    gnuplot> set data style lines          # plot using lines

#### Overlaying Multiple Plots

    gnuplot> plot sin(x), x**2/50-1

#### Overlaying Multiple Plots with Data

    gnuplot> plot  "/tmp/stats.txt" using 5 title "sentencelength", "/tmp/stats.txt" using 6 title "ratio"


#### Plotting with 2 axes

    gnuplot> set y2range [1:10]
    gnuplot> set y2range auto
    gnuplot> set y2tics border
    gnuplot> plot  "/tmp/stats.txt" using 5 title "sentencelength", "/tmp/stats.txt" using 6 title "ratio" axes x1y2


#### Output

    gnuplot> set terminal x11      # default, on screen

#### Postscript

    gnuplot> set output "test.ps"
    gnuplot> set terminal postscript [color] [solid]
    # color - default is monochrome
    # solid - solid lines instead of dashed default
    gnuplot> replot

### Curve Fitting

- e.g. Fit the dat in “force.dat” with a function

        gnuplot> f1(x) = a1*tanh(x/b1)     # define the function to be fit
        gnuplot> a1 = 300; b1 = 0.005;     # initial guess for a1 and b1
        gnuplot> fit f1(x) 'force.dat' using 1:2 via a1, b1


### Regression

#### Linear Regression

- Define the linear function

        gnuplot> f(x) = a*x + b

- Compute the regression line

        gnuplot> fit f(x) "test.data" via a,b

- Plot the line and the data

        
        gnuplot> plot f(x), "test.data"