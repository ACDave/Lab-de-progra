#!/bin/bash
sub="Prueba"
to="jose.hernandezsld@uanl.edu.mx"
mess="Holis"
from="erick.arredondocn@uanl.edu.mx"
pass="---"
name="Erick Arredondo"

echo $mess | \
-S ssl-verify=ignore \
-S smtp-auth=login \
-S smtp=smtp://smtp.office365.com:587 \
-S from=$From \
-S smtp-auth-user=$From \
-S smtp-auth-password=$Pass \
-S ssl-verify=ignore\
$To