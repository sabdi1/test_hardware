% Subscribing to oymotion_quat message
cuff_gesture     = rossubscriber('/oymotion_gest','std_msgs/Int16');
pause(1)


% % --------------------------------------------------------------------% 

first_time = true;

while true

    gest = cuff_gesture.LatestMessage.Data;
    
    rotm = quat2rotm(quat);

    if first_time
        
        % --------------------------------------------------------------- %
        %                      GESTURE VISUALIZATION
        % --------------------------------------------------------------- %   
        
        gest_number = ['Gesture: ' num2str(gest)];
        t = text(4,5,gest_number);
        
        figure
        
        first_time = false;
        
    else
        
        set(t,'String',['Gesture: ' num2str(gest)])

    end
end