select person.firstname,person.lastname,address.city,address.state from address
right join person
on person.personid=address.personid