%% Visualize_oymotion_orientation.m
% Script to show orientation of oymotion cuff via a 3D cube

% % --------------------------------------------------------------------% %

% Cube Size
Length = 2;
Width  = 2; 
Height = 2;

% UDP port
port = 5006;

% % --------------------------------------------------------------------% %

% Setting up and opening udp port
u = udp('localhost',port);
fopen(u);

l = 0.5*Length;
w = 0.5*Width;
h = 0.5*Height;

% Cube Corners
A = [-l -w  h];
B = [ l -w  h];
C = [ l  w  h];
D = [-l  w  h]; 
E = [-l -w -h];
F = [ l -w -h];
G = [ l  w -h];
H = [-l  w -h];

% Cube Faces
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
