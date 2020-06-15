<template>
    <mu-col span="4" xl="2" class="rooms-list">
        <div v-for="room in rooms">
            <h3 @click="openDialog(room.id)">{{ room.creater.username }}</h3>
            <small>{{ room.date }}</small>
        </div>
    </mu-col>
</template>

<script>
    export default {
        name: "Room",
        data() {                // хранение списка комнат
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
            },
            openDialog(id) {
                this.$emit("openDialog", id)
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
    .rooms-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
</style>
