function [cuff] = init_oymotion_cuff()
%INIT_OYMOTION_CUFF Summary of this function goes here
%   Detailed explanation goes here

% Structure for Oymotion Cuff Orientation Data
cuff.orient.quat        = [0,0,0,0];    
cuff.orient.quat_offset = [0,0,0,0];

% Structure for Oymotion Cuff Gesture Data
cuff.gest.count = [0,0,0,0];

end

