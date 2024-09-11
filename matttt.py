x=30;
disp('Value of x')
disp(x)
y=((2^x)+(log(x)*sin(x)))/((exp(x))-(sqrt(x)));
disp('Value of y')
disp(y)

# COMPLEX NUMBERS 
clc
clear all
close all
x=(pi/4);
disp('Value of x')
disp(x)
e=cos(x)+(i*(sin(x)));
disp('Value of e')
disp(e)

# vector

clc
clear all
close all
disp('----- Row Vector -----')
x=[1 2 3];
disp('Value of x')
disp(x)
z=[4, 5, 6];
disp('Value of z')
disp(z)
disp('----- Column Vector -----')
y=[1;2;3];
disp('Value of y')
disp(y)
%Addition of two vectors
a=x+z;
%dot operator is not needed for addition
disp('Value of a')
disp(a)
%Error as Matrix dimension mismatch
b=x+y;

# scaler
clc
clear all
close all
x=[1 2 3];
disp('Value of x')
disp(x)
y=10;
disp('Value of y')
disp(y)
%Multiplication by a scalar
mul=x*y;
disp('Value of Scalar Multiplication')
disp(mul)

# multiplication
clc
clear all
close all
x=[1 2 3];
disp('Value of x')
disp(x)
y=[1;2;3];
disp('Value of y')
disp(y)
z=[4 5 6];
disp('Value of z')
disp(z)
%Multiplication of two matrices
a = x * y;
disp('Value of * Multiplication between x and y')
disp(a)
b = x .* z;
%dot operator used for element wise multiplication
disp('Value of .* Multiplication between x and z')
disp(b)



# %Create Linearly Spaced Elements
x=linspace(0,70,7);
disp('Value of x')
disp(x)

# circle
clc
clear all
close all
%Circle
r=5;
theta=linspace(0,2*pi,100);
%linspace(initial value,final value, no of elements)
x=r*cos(theta);
y=r*sin(theta);
plot(x,y)
hold on,plot(0,0,'black*') %plot different commands in single plot
%axis('equal')
title('Plot a circle with radius value of 5')
ylabel('y')
xlabel('x')
%axis off
%grid on
%legend('boundary','centre')

# plotting
clc
clear all
close all
%Other plotting
x=0:10:1000;
%initial value:difference:final value
y=x.^5;
plot(x,y)
title('Plot')
xlabel('x')
ylabel('y')
figure,semilogx(x,y)
title('semilogx Plot')
xlabel('x')
ylabel('y')
figure,semilogy(x,y)
title('semilogy Plot')
xlabel('x')
ylabel('y')
figure,loglog(x,y)
title('loglog Plot')
xlabel('x')
ylabel('y')


# clock
%clc
clear all
close all
disp('Date is...')
disp(date) % display date
%already present
disp(' ')
disp('Value of clock')
disp(clock)%clock already presnt
time=fix(clock); % get time as integers
disp('Value of time')
disp(time)
disp(' ')
hourstr=int2str(time(4)); % get the hour
%int2str - converts integer to string
minstr=int2str(time(5)); % get the minute
secstr=int2str(time(6));
timex = [hourstr ':' minstr ':' secstr]; % create the time string
disp('Time is...')
disp(timex) % display the time
disp(' ')
disp('Display all the variables used in program')
whos

# % Solve linear equations
[x,y]=solve('x+2*y=8','2*x+y=7');
whos
x=double(x);
y=double(y);
whos
disp(' ')
disp(['x = ',num2str(x)])
disp(['y = ',num2str(y)])

