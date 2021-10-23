%% Visualize_oymotion_orientation.m
% Script to show orientation of oymotion cuff via a 3D cube
clear all; close all; clc;

% % --------------------------------------------------------------------% %

% Subscribing to oymotion_quat message
cuff_orientation = rossubscriber('/oymotion_quat','std_msgs/Float64MultiArray');
cuff_emg         = rossubscriber('/oymotion_emg' ,'std_msgs/Float64MultiArray');
cuff_gesture     = rossubscriber('/oymotion_gest','std_msgs/Int16');
pause(1)

% Cube Size
Length = 2;
Width  = 2; 
Height = 2;

% % --------------------------------------------------------------------% 

dims = [Length, Width, Height];

ch1 = []; ch2 = []; ch3 = []; ch4 = [];
ch5 = []; ch6 = []; ch7 = []; ch8 = [];

emg_idx_vec = 8*((1:16) - 1);
data_length = 500;
first_time = true;

while true
    quat = cuff_orientation.LatestMessage.Data.';
    emg  = cuff_emg.LatestMessage.Data;
    gest = cuff_gesture.LatestMessage.Data;
    
    rotm = quat2rotm(quat);

    if first_time
        % --------------------------------------------------------------- %
        %                          EMG VISUALIZATION
        % --------------------------------------------------------------- %

        ch1 = emg(2 + emg_idx_vec).'; ch2 = emg(3 + emg_idx_vec).'; 
        ch3 = emg(4 + emg_idx_vec).'; ch4 = emg(5 + emg_idx_vec).';
        ch5 = emg(6 + emg_idx_vec).'; ch6 = emg(7 + emg_idx_vec).'; 
        ch7 = emg(8 + emg_idx_vec).'; ch8 = emg(9 + emg_idx_vec).';

        subplot(2,6,1); ch1_plot = plot(ch1); axis([0 data_length 0 255]);
        subplot(2,6,2); ch2_plot = plot(ch2); axis([0 data_length 0 255]);
        subplot(2,6,3); ch3_plot = plot(ch3); axis([0 data_length 0 255]);
        subplot(2,6,4); ch4_plot = plot(ch4); axis([0 data_length 0 255]);
        subplot(2,6,7); ch5_plot = plot(ch5); axis([0 data_length 0 255]);
        subplot(2,6,8); ch6_plot = plot(ch6); axis([0 data_length 0 255]);
        subplot(2,6,9); ch7_plot = plot(ch7); axis([0 data_length 0 255]);
        subplot(2,6,10); ch8_plot = plot(ch8); axis([0 data_length 0 255]);
        drawnow
                
        % --------------------------------------------------------------- %
        %                      ORIENTATION VISUALIZATION
        % --------------------------------------------------------------- %        
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

%         Top    = [C;D;H;G;C];
%         Bottom = [A;B;F;E;A];
%         Front  = [A;B;C;D;A];
%         Left   = [A;D;H;E;A];
%         Right  = [C;B;F;G;C];
%         Back   = [E;F;G;H;E];

        Top_Rot = Top*rotm;
        Bot_Rot = Bottom*rotm;
        Frt_Rot = Front*rotm;
        Lft_Rot = Left*rotm;
        Rgt_Rot = Right*rotm;
        Bck_Rot = Back*rotm;

        subplot(2,6,[5,6])
        hold on
        view(3)
        
        Patch_TOP = patch(Top_Rot(:,1),Top_Rot(:,2),Top_Rot(:,3),'r');
        Patch_BOT = patch(Bot_Rot(:,1),Bot_Rot(:,2),Bot_Rot(:,3),'g');
        Patch_FRT = patch(Frt_Rot(:,1),Frt_Rot(:,2),Frt_Rot(:,3),'y');
        Patch_LFT = patch(Lft_Rot(:,1),Lft_Rot(:,2),Lft_Rot(:,3),'b');
        Patch_RGT = patch(Rgt_Rot(:,1),Rgt_Rot(:,2),Rgt_Rot(:,3),'m');
        Patch_BCK = patch(Bck_Rot(:,1),Bck_Rot(:,2),Bck_Rot(:,3),'c');
        
        max_dim = max(dims);
        
        axis([-max_dim max_dim -max_dim max_dim -max_dim max_dim])
        axis square
        grid on

        xlabel('X-Axis')
        ylabel('Y-Axis')
        zlabel('Z-Axis')

        legend('Top','Bottom','Front', 'Left', 'Right', 'Back')
        
        % --------------------------------------------------------------- %
        %                      GESTURE VISUALIZATION
        % --------------------------------------------------------------- %   

        gest_plot = subplot(2,6,[11,12]);
        axis([-1 1 -1 1])
        set(gest_plot,'YTickLabel',[])
        set(gest_plot,'YTick',[])
        set(gest_plot,'XTickLabel',[])
        set(gest_plot,'XTick',[])

        gest_number = ['Gesture: ' num2str(gest)];
        t = text(-0.25,0,gest_number);
        
        first_time = false;
        
    else
        
        if length(ch1) > data_length
            ch1(1:16) = []; ch2(1:16) = []; ch3(1:16) = []; ch4(1:16) = []; 
            ch5(1:16) = []; ch6(1:16) = []; ch7(1:16) = []; ch8(1:16) = []; 
        end
        
        ch1 = [ch1,emg(2 + emg_idx_vec).']; ch2 = [ch2,emg(3 + emg_idx_vec).']; ch3 = [ch3,emg(4 + emg_idx_vec).']; ch4 = [ch4,emg(5 + emg_idx_vec).']; 
        ch5 = [ch5,emg(6 + emg_idx_vec).']; ch6 = [ch6,emg(7 + emg_idx_vec).']; ch7 = [ch7,emg(8 + emg_idx_vec).']; ch8 = [ch8,emg(9 + emg_idx_vec).']; 
        
        set(ch1_plot,'YData',ch1); set(ch2_plot,'YData',ch2); set(ch3_plot,'YData',ch3); set(ch4_plot,'YData',ch4);
        set(ch5_plot,'YData',ch5); set(ch6_plot,'YData',ch6); set(ch7_plot,'YData',ch7); set(ch8_plot,'YData',ch8);
        drawnow
        
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
        
        set(t,'String',['Gesture: ' num2str(gest)])

    end
end
