% This script creates a new flow field
% We need to initialize U1, U2, U3, TH and P

% Since we are starting with a new flow, set TIME_STEP=0
% If you are continuing an existing simulation, don't do this (unless you want to reset the timestep)
TIME_STEP=0;

U1=uinit(:,:,9999); % U1 is the velocity in the X direction
U2=vinit(:,:,9999); % U2 is the velocity in the Y direction
U3=zeros(NX,NY); % U3 is the velocity in the Z direction
P=zeros(NX,NY); % P is the pressure
PHI=zeros(NX,NY); % PHI is a temporary variable used to make the velocity divergence free

TH=zeros(NX,NY,N_TH)+1;

% ********* User Input ********

% Start with an unstable buoyancy profile, here TH is buoyancy
for i=1:NX
for j=1:NY
  
end
end

% Example: For internal waves, create a stable buoyancy profile
% for i=1:NX
% for j=1:NY
%  TH(i,j,:)=GYF(j);
%  TH(i,j,:)=TH(i,j,:)+0.2*exp(-(GXF(i)-LX/2)^2/0.2^2-(GYF(j)-LY/2)^2/0.2^2); % optionally, add an initial perturbation
% end
% end

% Example: initialize tracers from a color image
% A=imread('image.jpg');
% B=imresize(A,[NX NY]);
% TH=double(B);
% TH=permute(TH,[2,1,3]);

% Add a random perturbation to the velocity
% U1=U1+0.001*(rand(NX,NY)-0.5);
% U2=U2+0.001*(rand(NX,NY)-0.5);


% ********* End of User input *********

% Make sure that the new flow field satisfies the boundary conditions
rk_apply_bc_vel

