% fig_hand = plot_cube_sa([2,2,2],[0,0,0,]);

 A = [0 0 0];
 B = [1 0 0];
 C = [0 1 0];
 D = [0 0 1];
 E = [0 1 1];
 F = [1 0 1];
 G = [1 1 0];
 H = [1 1 1];
 P = [A;B;F;H;G;C;A;D;E;H;F;D;E;C;G;B];
 figure;
 plot3(P(:,1),P(:,2),P(:,3))
 axis([-1 2 -1 2 -1 2])
 
roll = -0.3064; pitch = -1.2258; yaw = 9.8066;
dcm = angle2dcm(yaw, pitch, roll);
P = P*dcm;
figure;
plot3(P(:,1),P(:,2),P(:,3)) % rotated cube
axis([-1 2 -1 2 -1 2])

%%
Top = [A;B;F;H;G;C;A;D;E;H;F;D;E;C;G;B];

eul = [0 pi/4 0];
qZYX = eul2quat(eul)

quat = [0.7071 0.7071 0 0];
rotm = quat2rotm(qZYX)

Top_Rot = Top*rotm;

figure;
hold on
plot3(Top(:,1),Top(:,2),Top(:,3),'b')
plot3(Top_Rot(:,1),Top_Rot(:,2),Top_Rot(:,3),'r')
view(3)

%%
 A = [-1 -1 -1];
 B = [1 -1 -1];
 C = [-1 1 -1];
 D = [-1 -1 1];
 E = [-1 1 1];
 F = [1 -1 1];
 G = [1 1 -1];
 H = [1 1 1];

Top = [A;B;F;H;G;C;A;D;E;H;F;D;E;C;G;B];

ang = 0:pi/90:2*pi;

eul = [0 pi/4 0];
qZYX = eul2quat(eul);
rotm = quat2rotm(qZYX);
Top_Rot = Top*rotm;

figure;
hold on
plot3(Top(:,1),Top(:,2),Top(:,3),'b');
Q_cube = plot3(Top_Rot(:,1),Top_Rot(:,2),Top_Rot(:,3),'r');
view(3)
axis()
axis([-2 2 -2 2 -2 2])

x = [0 1 1 0];
y = [0 0 1 1];
patch(x,y,'red')

for ii = 1:length(ang)
    eul = [0 ang(ii) 0];
    qZYX = eul2quat(eul)
    rotm = quat2rotm(qZYX)
    Top_Rot = Top*rotm;  
    set(Q_cube,'XData',Top_Rot(:,1))
    set(Q_cube,'YData',Top_Rot(:,2))
    set(Q_cube,'ZData',Top_Rot(:,3))
    drawnow
    pause(0.1)
end

%% 

% Top face RED
A = [-1 -1 1];
B = [ 1 -1 1];
C = [ 1  1 1];
D = [-1  1 1];
 
% Bottom face GREEN
E = [-1 -1 -1];
F = [ 1 -1 -1];
G = [ 1  1 -1];
H = [-1  1 -1];
 
Top    = [A;B;C;D;A];
Bottom = [E;F;G;H;E];
Front  = [E;F;B;A;E];
Left   = [E;A;D;H;E];
Right  = [F;G;C;B;F];
Back   = [H;G;C;D;H];

ang = 0:pi/9:2*pi;

eul = [0 pi/4 0];
qZYX = eul2quat(eul);
rotm = quat2rotm(qZYX);

Top_Rot = Top*rotm;
Bot_Rot = Bottom*rotm;
Frt_Rot = Front*rotm;
Lft_Rot = Left*rotm;
Rgt_Rot = Right*rotm;
Bck_Rot = Back*rotm;

figure;
hold on
view(3)
axis([-2 2 -2 2 -2 2])
axis square
grid on

xlabel('X-Axis')
ylabel('Y-Axis')
zlabel('Z-Axis')

Patch_TOP = patch(Top_Rot(:,1),Top_Rot(:,2),Top_Rot(:,3),'r')
Patch_BOT = patch(Bot_Rot(:,1),Bot_Rot(:,2),Bot_Rot(:,3),'g')
Patch_FRT = patch(Frt_Rot(:,1),Frt_Rot(:,2),Frt_Rot(:,3),'y')
Patch_LFT = patch(Lft_Rot(:,1),Lft_Rot(:,2),Lft_Rot(:,3),'b')
Patch_RGT = patch(Rgt_Rot(:,1),Rgt_Rot(:,2),Rgt_Rot(:,3),'m')
Patch_BCK = patch(Bck_Rot(:,1),Bck_Rot(:,2),Bck_Rot(:,3),'c')


eul = [0 ang 0];
z = zeros(length(ang),1);

eul_angs = [[ang.' z z]; [z ang.' z];[z z ang.'];[ang.' ang.' ang.']]

for ii = 1:length(eul_angs)
    eul = eul_angs(ii,:);
    qZYX = eul2quat(eul);
    rotm = quat2rotm(qZYX);

    Top_Rot = Top*rotm;
    Bot_Rot = Bottom*rotm;
    Frt_Rot = Front*rotm;
    Lft_Rot = Left*rotm;
    Rgt_Rot = Right*rotm;
    Bck_Rot = Back*rotm;  

    set(Patch_TOP,'XData',Top_Rot(:,1))
    set(Patch_TOP,'YData',Top_Rot(:,2))
    set(Patch_TOP,'ZData',Top_Rot(:,3))
    
    set(Patch_BOT,'XData',Bot_Rot(:,1))
    set(Patch_BOT,'YData',Bot_Rot(:,2))
    set(Patch_BOT,'ZData',Bot_Rot(:,3))
    
    set(Patch_FRT,'XData',Frt_Rot(:,1))
    set(Patch_FRT,'YData',Frt_Rot(:,2))
    set(Patch_FRT,'ZData',Frt_Rot(:,3))
    
    set(Patch_LFT,'XData',Lft_Rot(:,1))
    set(Patch_LFT,'YData',Lft_Rot(:,2))
    set(Patch_LFT,'ZData',Lft_Rot(:,3))
    
    set(Patch_RGT,'XData',Rgt_Rot(:,1))
    set(Patch_RGT,'YData',Rgt_Rot(:,2))
    set(Patch_RGT,'ZData',Rgt_Rot(:,3))
    
    set(Patch_BCK,'XData',Bck_Rot(:,1))
    set(Patch_BCK,'YData',Bck_Rot(:,2))
    set(Patch_BCK,'ZData',Bck_Rot(:,3))
    drawnow
    pause(0.05)
end
