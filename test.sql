SELECT 
    e.id,
    e.gamer_id,
    e.description AS game_name,
    e.date,
    e.time,
    u.first_name || ' ' || u.last_name as full_name
FROM levelupapi_event AS e
JOIN levelupapi_gamer AS g ON g.id = e.gamer_id
JOIN auth_user AS u ON u.id = g.user_id;



