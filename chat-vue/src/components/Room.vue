<template>
    <div>
        <ul>
            <li v-for="room in rooms">
                <h3>{{ room.creater.username }}</h3>
                {{ room.date }}
            </li>
        </ul>
    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Room",
        data() {        // хранение списка наших комнат
            return {
                rooms: '',
            }
        },
        created() {     // когда загрузиться наш компонент, выполнить
            $.ajaxSetup({                //  в ajaxSetup заносим в headers
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                // "Authorization": "Token 6a57d9af66fcf68b9fac066e67d4a450f5cf667a"
            });
            this.loadRoom()         // запуск ф-ции loadRoom
        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                    type: "GET",
                    success: (response) => {            // при удачнои ответе
                        this.rooms = response.data.date      // присвоение переменной rooms ответа
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
