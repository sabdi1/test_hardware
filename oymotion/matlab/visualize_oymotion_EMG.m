%% Visualize_oymotion_orientation.m
% Script to show orientation of oymotion cuff via a 3D cube

% % --------------------------------------------------------------------% %

% Subscribing to oymotion_emg message
cuff_emg = rossubscriber('/oymotion_emg','std_msgs/Float64MultiArray');
pause(1)

first_time = true;

ch1 = []
ch2 = []
ch3 = []
ch4 = []
ch5 = []
ch6 = []
ch7 = []
ch8 = []

tstart = datevec(now);
emg_idx_vec = 8*((1:16) - 1);
data_length = 500;

while true
     
    if first_time
        emg  = cuff_emg.LatestMessage.Data;

        ch1 = emg(2 + emg_idx_vec).'; ch2 = emg(3 + emg_idx_vec).'; ch3 = emg(4 + emg_idx_vec).'; ch4 = emg(5 + emg_idx_vec).';
        ch5 = emg(6 + emg_idx_vec).'; ch6 = emg(7 + emg_idx_vec).'; ch7 = emg(8 + emg_idx_vec).'; ch8 = emg(9 + emg_idx_vec).';

        subplot(2,4,1); ch1_plot = plot(ch1); axis([0 data_length 0 255]);
        subplot(2,4,2); ch2_plot = plot(ch2); axis([0 data_length 0 255]);
        subplot(2,4,3); ch3_plot = plot(ch3); axis([0 data_length 0 255]);
        subplot(2,4,4); ch4_plot = plot(ch4); axis([0 data_length 0 255]);
        subplot(2,4,5); ch5_plot = plot(ch5); axis([0 data_length 0 255]);
        subplot(2,4,6); ch6_plot = plot(ch6); axis([0 data_length 0 255]);
        subplot(2,4,7); ch7_plot = plot(ch7); axis([0 data_length 0 255]);
        subplot(2,4,8); ch8_plot = plot(ch8); axis([0 data_length 0 255]);

        drawnow
        
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

    end
    
    
    emg  = cuff_emg.LatestMessage.Data;
    
    fprintf('@ etime = %f : emg  = [%f, %f, %f, %f, %f, %f, %f, %f] \n', etime(datevec(now),tstart), emg(2), emg(3), emg(4), emg(5), emg(6), emg(7), emg(8), emg(9));

end
