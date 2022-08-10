-- converts database htbn_0c_0 character set and collation to utf8
-- converts first_table table in htbn_0c_0 database character set to utf8
ALTER DATABASE htbn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE htbn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE htbn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
