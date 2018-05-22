Categories: matlab
Tags: 


clc;
figure;
hold on;
grid on;
xlabel('x');
ylabel('y');
zlabel('z');


% axes
lims = axis;
plot3(lims(1:2),[0 0],[0 0], 'LineWidth', 1.5, 'Color', 'blue') % x axis
plot3([0 0],lims(3:4),[0 0], 'LineWidth', 1.5, 'Color', 'green') % y axis
plot3([0 0],[0 0],lims(5:6), 'LineWidth', 1.5, 'Color', 'red') % z axis



% print dots
scatter3(a(:,1), a(:,2), a(:,3));