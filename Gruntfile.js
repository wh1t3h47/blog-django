module.exports = function(grunt) {
    grunt.initConfig({
        uncss: {
            dist: {
                files: [{
                    nonull: true,
                    src: ['https://freiruidepine.com.br/'],
                    dest: 'FreiRui/static/css/purified.css'
                }]
            }, 
            options: {
                ignoreSheets : [/fonts.googleapis/, /fonts.gstatic.com/, /freiruidepine.com.br/],
                // stylesheets: ['/static/styles/styles.css'],
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-uncss');

    // Default tasks.
    grunt.registerTask('default', ['uncss']);

};
