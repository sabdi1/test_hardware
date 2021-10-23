function [fig_hand] = plot_cube_sa(LWH, origin)

    x_min = origin(1) - LWH(1)/2;
    x_max = origin(1) + LWH(1)/2;
    y_min = origin(2) - LWH(2)/2;
    y_max = origin(2) + LWH(2)/2;
    z_min = origin(3) - LWH(3)/2;
    z_max = origin(3) + LWH(3)/2;

    XYZ1 = [x_min, y_min, z_min;...
            x_max, y_min, z_min;...
            x_max, y_max, z_min;...
            x_min, y_max, z_min;
            x_min, y_min, z_min;];
       
       
    XYZ2 = [x_min, y_min, z_max;...
            x_max, y_min, z_max;...
            x_max, y_max, z_max;...
            x_min, y_max, z_max;
            x_min, y_min, z_max;];

       
    XYZ3 = [x_min, y_min, z_max;...
            x_max, y_min, z_max;...
            x_max, y_max, z_max;...
            x_min, y_max, z_max;
            x_min, y_min, z_max;];
        
    fig_hand = figure;
    hold on
    plot3(XYZ1(:,1),XYZ1(:,2),XYZ1(:,3))
    plot3(XYZ2(:,1),XYZ2(:,2),XYZ2(:,3))
    plot3(XYZ3(:,1),XYZ3(:,2),XYZ3(:,3))

    
end