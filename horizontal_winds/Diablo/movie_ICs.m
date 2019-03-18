% Show a movie

figure(1);
for t = 1:9999
    surf(uinit(:,:,t))
    
%     colorbar
%     caxis([-0.1 0.05])
    mov(t)=getframe;
 
end

movie(mov,1,20);