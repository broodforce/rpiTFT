%% Parameters from GPS
v1= 1;                                  % Initial velocity
v2= 1.05;                               % Final velocity

theta1=pi/4;                            % Initial angle
% https://www.reddit.com/r/EngineeringStudents/comments/3i7v3g/calculate_lateral_acceleration_from_gps_data/
theta2=pi/4+.05;                        % Final angle

t1=1.00;                                % Initial timestamp
t2=1.01;                                % Final timestamp

%% Compute the acceleration
% Find the initial velocity vector
% in global reference frame [X Y] 
v1_vec=v1*[cos(theta1);sin(theta1)]; 

% Find the final velocity vector
% in global reference frame [X Y] 
v2_vec=v2*[cos(theta2);sin(theta2)];

% Find the average angle
theta_avg=(theta1+theta2)/2;            

% Compute a rotation matrix based on the average angle
r=[cos(theta_avg) -sin(theta_avg);      
   sin(theta_avg) cos(theta_avg)];

% Compute acceleration vector in global reference frame [X Y] 
a=(v2_vec-v1_vec)/(t2-t1);              

% De-rotate acceleration using transpose of rotation matrix
% to get vector in vehicle reference frame [x, y]
a_comp=r'*a;  
