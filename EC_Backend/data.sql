ALTER TABLE t_menu AUTO_INCREMENT = 1;
insert into t_menu (id, name, level) value (0, 'all', 0);
insert into t_menu (id, name, level, pid) value (0, 'user management', 1, 1);
insert into t_menu (id, name, level, pid) value (0, 'authority management', 1, 1);
insert into t_menu (id, name, level, pid) value (0, 'product management', 1, 1);
insert into t_menu (id, name, level, pid) value (0, 'order-form management', 1, 1);
insert into t_menu (id, name, level, pid) value (0, 'data statistics', 1, 1);
insert into t_menu (id, name, level, pid, path) value (21, 'user list', 2, 2, '/user_list');
insert into t_menu (id, name, level, pid, path) value (31, 'role list', 2, 3, '/role_list');
insert into t_menu (id, name, level, pid, path) value (32, 'permission list', 2, 3, '/permission_list');
insert into t_menu (id, name, level, pid, path) value (41, 'product list', 2, 4, '/product_list');
insert into t_menu (id, name, level, pid, path) value (42, 'category list', 2, 4, '/category_list');
