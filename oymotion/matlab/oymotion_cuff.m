classdef oymotion_cuff
    %OYMOTION_CUFF Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        cuff_orientation = rossubscriber('/oymotion_quat','std_msgs/Float64MultiArray');
        cuff_gesture     = rossubscriber('/oymotion_gest','std_msgs/Int16');
        cuff_emg         = rossubscriber('/oymotion_emg' ,'std_msgs/Float64MultiArray');

        quat = [0,0,0,0];
        gest = 0;
        emg = [];
        
        quat_offset = [0,0,0,0];
        last_gest   = 0;
        gest_count  = [0,0,0,0,0,0,0,0];
    end
    
    methods
        % Constructor
        function obj = oymotion_cuff()
        end
        
        function obj = update_cuff_data(obj)
            obj.quat = obj.cuff_orientation.LatestMessage.Data.';
            obj.gest = obj.cuff_gesture.LatestMessage.Data.';
            obj.emg  = obj.cuff_emg.LatestMessage.Data;

            if (obj.gest ~= 0) && (obj.last_gest == 0)
                obj = update_gest_count(obj,obj.gest)
            end
            
            obj.last_gest = obj.gest;
            
        end
                       
        function obj = update_gest_count(obj,gest_num)
            obj.gest_count(gest_num) = obj.gest_count(gest_num) + 1;
            obj = check_gest(obj);
        end
        
        function obj = check_gest(obj)
            % If gesture 1 x3, set quaternion offset
            if obj.gest_count(1) == 3
                obj.quat_offset = obj.cuff_orientation.LatestMessage.Data.';
                obj.quat = obj.quat .* obj.quat_offset;           

                obj.gest_count(1) = 0;
            elseif obj.gest_count(2) == 3
                obj.quat_offset = [0,0,0,0]
                obj.gest_count(2) = 0;
            end
        end
    end
end

