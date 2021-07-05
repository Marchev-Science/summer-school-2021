# Declare variables of different types
# Numeric
x <- 28
class(x)

# String
y <- "R is Fantastic"
class(y)

# Boolean
z <- TRUE
class(z)

# Print variable x
x <- 42
x

#Example:
y  <- 10
y

#Example:
# We call x and y and apply a subtraction
x-y

# Numerical
vec_num <- c(1, 10, 49)
vec_num

# Character 
vec_chr <- c("a", "b", "c")
vec_chr

# Boolean 
vec_bool <-  c(TRUE, FALSE, TRUE)
vec_bool

# Example:

# Create the vectors
vect_1 <- c(1, 3, 5)
vect_2 <- c(2, 4, 6)
# Take the sum of A_vector and B_vector
sum_vect <- vect_1 + vect_2
# Print out total_vector
sum_vect

# Slice the first five rows of the vector
slice_vector <- c(10,9,8,7,6,5,4,3,2,1)
pesho  <- slice_vector[2:5]
pesho

# Faster way to create adjacent values
c(1:10)

# Addition
3 + 4

# Multiplication
3*5

# Division
(5+5)/2

# Exponentiation
2^5
2**5

# Modulo
28%%6

# Create a vector from 1 to 10
logical_vector <- c(1:10)
logical_vector
logical_vector>5

# Print value strictly above 5
logical_vector[(logical_vector>5)]

# Print 5 and 6
logical_vector <- c(1:10)
logical_vector[(logical_vector>4) & (logical_vector<7)]

# Construct a matrix with 5 rows that contain the numbers 1 up to 10 and byrow =  TRUE 
matrix_a <-matrix(1:10, byrow = TRUE, nrow = 5)
matrix_a

# Print dimension of the matrix with dim()
dim(matrix_a)

# Construct a matrix with 5 rows that contain the numbers 1 up to 10 and byrow =  FALSE
matrix_b <-matrix(1:10, byrow = FALSE, nrow = 5)
matrix_b

# Print dimension of the matrix with dim()
dim(matrix_b)

# You can also create a 4x3 matrix using ncol. R will create 3 columns and fill the row from top to bottom.
matrix_c <-matrix(1:12, byrow = FALSE, ncol = 3)
matrix_c

dim(matrix_c)

# Add a Column to a Matrix with the cbind()

# concatenate c(1:5) to the matrix_a
matrix_a1 <- cbind(c(1:5),matrix_a)
# Check the dimension
matrix_a1

dim(matrix_a1)

# Concatenate matrix
matrix_a2 <-matrix(13:24, byrow = FALSE, ncol = 3)

matrix_c <-matrix(1:12, byrow = FALSE, ncol = 3)
matrix_d <- cbind(matrix_a2, matrix_c)
matrix_d

dim(matrix_d)

# Append
matrix_c <-matrix(1:12, byrow = FALSE, ncol = 3)
# Create a vector of 3 columns
add_row <- c(1:3)
# Append to the matrix
matrix_c <- rbind(matrix_c, add_row)
matrix_c
# Check the dimension
dim(matrix_c)

matrix_c

slice1 <- matrix_c[1,2]
slice1

slice2 <- matrix_c[1:3,2:3]
slice2

slice3 <- matrix_c[,1]
slice3

slice4 <- matrix_c[1,]
slice4

# Create gender vector
gender_vector <- c("Male", "Female", "Female", "Male", "Male")
class(gender_vector)

# Convert gender_vector to a factor
factor_gender_vector <-factor(gender_vector)
factor_gender_vector

class(factor_gender_vector)

# Nominal Categorical Variable
# A categorical variable has several values but the order does not matter. 

# Create a color vector
color_vector <- c('blue', 'red', 'green', 'white', 'black', 'yellow')
# Convert the vector to factor
factor_color <- factor(color_vector)
factor_color

# Create Ordinal categorical vector 
day_vector <- c('evening', 'morning', 'afternoon', 'midday', 'midnight', 'evening')
# Convert `day_vector` to a factor with ordered level
factor_day <- factor(day_vector, order = TRUE, levels =c('morning', 'midday', 'afternoon', 'evening', 'midnight'))
# Levels: morning < midday < afternoon < evening < midnight
# Print the new variable
factor_day

# Count the number of occurence of each level
summary(factor_day)

# Continuous Variables
dataset <- mtcars
class(dataset$mpg)
dataset$mpg

# Create a, b, c, d variables
a <- c(10,20,30,40)
b <- c('book', 'pen', 'textbook', 'pencil_case')
c <- c(TRUE,FALSE,TRUE,FALSE)
d <- c(2.5, 8, 10, 7)
# Join the variables to create a data frame
df <- data.frame(a,b,c,d)
df

# Name the data frame
names(df) <- c('ID', 'items', 'store', 'price')
df

# Print the structure
str(df)

# Slice Data Frame
## Select row 1 in column 2
df[1,2]

## Select Rows 1 to 2
df[1:2,]

## Select Columns 1
df[,1]

## Select Rows 1 to 3 and columns 3 to 4
df[1:3, 3:4]

# Slice with columns name
df[, c('ID', 'store')]

#Append a Column to Data Frame

# Create a new vector
quantity <- c(10, 35, 40, 5)
# Add `quantity` to the `df` data frame
df$quantity <- quantity
df

# Select the column ID
df$ID

square_function<- function(n) 
{
  # compute the square of integer `n`
  n^2
}  
# calling the function and passing value 4
square_function(4.32)

set.seed(0)
## Create the data
x = rnorm(1000)
x

ts <- cumsum(x)
ts

## Stationary the serie
diff_ts <- diff(ts)
par(mfrow=c(1,2))


# Plot the series
plot(ts, type='l')
plot(diff(ts), type='l')
dt <- cars

## number columns
length(dt)

## number rows
length(dt[,1])

# sequence of number from 44 to 55 both including incremented by 1
x_vector <- seq(45,55, by = 1)
x_vector

#logarithm
log(x_vector)

#exponential
exp(x_vector)

#squared root
sqrt(x_vector)

#factorial
factorial(x_vector)

speed <- dt$speed
speed

# Mean speed of cars dataset
mean(speed)

# Median speed of cars dataset
median(speed)

# Variance speed of cars dataset
var(speed)

# Standard deviation speed of cars dataset
sd(speed)

# Standardize vector speed of cars dataset
head(scale(speed), 5)

# Quantile speed of cars dataset
quantile(speed)

# Summary speed of cars dataset
summary(speed)

# Case:
# Imagine we have three different kind of products with different VAT applied:
# We can write a chain to apply the correct VAT rate to the product a customer bought.

# Create a, b, c, d variables
Categories <- c('A','B','C')
Products <- c('Book, magazine, newspaper, etc..', 'Vegetable, meat, beverage, etc..', 'Tee-shirt, jean, pant, etc..')
VAT <- c('8%','10%','20%')
# Join the variables to create a data frame
df <- data.frame(Categories,Products,VAT)
df

category <- 'A'
price <- 10
if (category =='A'){
  cat('A VAT rate of 8% is applied.','The total price is',price *1.08)  
} else if (category =='B'){
    cat('A VAT rate of 10% is applied.','The total price is',price *1.10)  
} else {
    cat('A VAT rate of 20% is applied.','The total price is',price *1.20)  
}

# Example: iterate over all the elements of a vector and print the current value.

# Create fruit vector
fruit <- c('Apple', 'Orange', 'Passion fruit', 'Banana')
# Create the for statement
for ( i in fruit){ 
 print(i)
}

PATH <- 'https://raw.githubusercontent.com/guru99-edu/R-Programming/master/mtcars.csv'                
df <- read.csv(PATH, header =  TRUE, sep = ',')
df

length(df)

class(df$X)

# Install and activate library `readxl`  
require(readxl)
library(readxl)
# We can import the spreadsheets from the readxl library and count the number of columns in the first sheet.
readxl_example()

# Store the path of `datasets.xlsx`
example <- readxl_example("datasets.xlsx")
# Import the spreadsheet
df <- read_excel(example)
df

# Count the number of columns
length(df)

# Example
write.csv(df, "table_VAT.csv")

# read some data
acs <- read.csv(url("http://stat511.cwick.co.nz/homeworks/acs_or.csv"))
acs

# Scatter plot
plot(x = acs$age_husband , y = acs$age_wife, type = 'p')

# Histogram
hist(acs$number_children)

# Bar Plots
counts <- table(acs$bedrooms)
barplot(counts, main="Bedrooms Distribution",  xlab="Number of Bedrooms")

png(file="saving_plot2.png",width=600, height=600)
counts <- table(acs$bedrooms)
barplot(counts, main="Bedrooms Distribution",  xlab="Number of Bedrooms")
dev.off()

install.packages("readxl", lib='C:/Users/Junior/Documents/R/win-library/3.6')
install.packages("tseries", lib='C:/Users/Junior/Documents/R/win-library/3.6')
install.packages("forecast", lib='C:/Users/Junior/Documents/R/win-library/3.6')
install.packages("data.table", lib='C:/Users/Junior/Documents/R/win-library/3.6')
install.packages("TTR", lib='C:/Users/Junior/Documents/R/win-library/3.6')

library(readxl)
library(forecast)
library(tseries)
library(data.table)
library(TTR)

# Load the data
data <- read_xlsx("01. Belgium.xlsx", sheet =1, col_names = TRUE)
# Data preparation
colnames(data) <- c("GEO/TIME", "TimeT", "Y", "X1", "X2", "NOCOL", "CODE", "COUNTRY", "START", "END","TOTOAL_ROWS", "TRAIN_ROWS", "TEST_ROWS")
data

total_rows <- as.numeric(data[1,11])
train_rows <- as.numeric(data[1,12])
test_rows <- as.numeric(data[1,13])
workingNumber<-train_rows+1
data <- data[ ,-1]
data <- data[ , -c(5:12)]
data

i=1
current_row=1
working_Y <-rep(0, total_rows)
working_Y <- as.data.frame(working_Y)
working_SMA <- as.data.frame(shift(SMA(data[,2],n=3),1))
for (i in 1:total_rows) {
  if (current_row <= train_rows ) {
    working_Y[i,1] <- data[i,2]
  }else{ working_Y[i,1] <- working_SMA[i,1]}
  
  working_SMA <- as.data.frame(shift(SMA(working_Y[,1],n=3),1))
  current_row = current_row + 1
}

forecast11 <- as.data.frame(shift(SMA(working_Y, 3),1))
forecast11


# Calculate mean relative error
abs11yf <- abs(forecast11-data[,2])
abs11y <- abs(data[,2])
R11 <<- sum(abs11yf[4:train_rows,1])/sum(abs11y[4:train_rows,1])
S11 <<- sum(abs11yf[(train_rows+1):total_rows,1])/sum(abs11y[(train_rows+1):total_rows,1])

plot.ts(data[,2], type="l", col = "blue", main = "Simple moving average (3 periods) : F(t)=(Y(t-1)+Y(t-2)+Y(t-3))/3" )
lines(forecast11, type="l", col = "red")

cat("\n","\n","Simple moving average (3 periods) : F(t)=(Y(t-1)+Y(t-2)+Y(t-3))/3:  ","\n", "R =", round(R11*100, digits = 2), "%;", "  S =", round(S11*100, digits = 2))


