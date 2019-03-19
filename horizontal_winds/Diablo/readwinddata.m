%read csv data

Udata = csvread('velocity_x.csv');
Vdata = csvread('velocity_y.csv');

[N,M] = size(Udata);
% M is index, N is timestep 1 to 10,000
%trim data
Udata = Udata(2:N,2:M);
Vdata = Vdata(2:N,2:M);
% Now read into a 3x3 array
uinit = zeros(9,9,9999);
vinit = zeros(9,9,9999);
for i = 1:9999
    counter = 1;
    for j = 1:81
        uinit(mod(j-1,9)+1,counter,i) = Udata(i,j);
        vinit(mod(j-1,9)+1,counter,i) = Vdata(i,j);
        if mod(j,9)==0;
            counter = counter+1;
        end
    end
    
end
        