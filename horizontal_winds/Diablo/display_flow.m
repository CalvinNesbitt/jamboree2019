% This script is called every N_DISP_FLOW timesteps, and writes something to the screen

n_display=floor((TIME_STEP-1)/N_DISP_FLOW)+1; % Calculate the index for making a movie file
clf;

% ******** User Input *********
% Change the following lines to plot whatever you like during the simulation

% Plot scalar n=1 (in this example, buoyancy)
pcolor(GX(ii),GY(jj),U1(ii,jj)')%, shading interp; 
xlabel('X');
ylabel('Y');
title('U1');
caxis([0 1]);
axis([GX(ii(1)) GX(ii(end)) GYF(jj(1)) GYF(jj(end))]);
colorbar

% Example: plot a color image from a scalar array with (r,g,b) components
% imagesc(permute(min(max(TH/255,0),1),[2,1,3])); axis equal; axis tight;

% ******** End of User Input *********

% Here, we save the frame to a moviefile to replay after the simulation is done
mov(n_display)=getframe;
% And pause for a short amount of time to make sure that there is enough time for the screen to refresh
pause(0.01);

