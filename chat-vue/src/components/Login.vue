<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password" type="password" placeholder="Пароль"/>
        <button @click="setLogin">Войти</button>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/create/',
                    type: "POST",
                    data: {             //данные которые передаем на бек-енд
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        // console.log(response.data.attributes.auth_token)
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)       // сохранение токена в сессионное хранилище
                        this.$router.push({name: "home"})       // перенапрвление на страницу home
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
