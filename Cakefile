require 'flour'
fs = require 'fs'
sys = require('sys')
{spawn, exec} = require 'child_process'

coffe_src = "coffee"
less_src = "less"

js_out = "static/js"
css_out = "static/css"
watch_files = false
color_filter = (string, tag) ->
    return ("\n" + tag).grey + string.toString().replace(/(\r\n|\n|\r)/gm, ("\n" + tag).grey)
compile_recursive = (dir, out_dir, ext, ext_out=ext, orig_dir) ->
    dirs = []
    if orig_dir
        out_apn = out_dir + "/" + dir.substring orig_dir.length+1
    else
        out_apn = out_dir
        orig_dir = dir

    # check our out APN
    if not fs.exists out_apn
        fs.mkdir out_apn
    console.log "Entering directory '#{dir}' to compile #{ext} files to #{out_apn}".blue
    for file in fs.readdirSync dir
        apn = "#{dir}/#{file}"
        stat = fs.statSync apn
        bits = file.split "."
        # add to our list of directories if its a dir
        if stat.isDirectory()
            dirs.push(apn)
            continue
        # compile it if it's the type we're looking for
        if bits[bits.length - 1] == ext
            dest = "#{out_apn}/#{bits[0]}.#{ext_out}"
            try
                if (fs.statSync dest).mtime.getTime < stat.mtime.getTime
                    compile apn, dest
                else
                    console.log "Up To Date ".yellow + "#{apn} -> #{dest}"
            catch error
                compile apn, dest
            if watch_files
                fs.watchFile apn, { persistent: true, interval: 3000 }, compile_specific.bind(null, apn, dest)
    compile_recursive dir, out_dir, ext, ext_out, orig_dir for dir in dirs

compile_specific = (src, dest, action, filename) ->
  compile src, dest

rmDir = (dirPath) ->
  try
    files = fs.readdirSync(dirPath)
  catch e
    return
  if files.length > 0
    i = 0

    while i < files.length
      filePath = dirPath + "/" + files[i]
      if fs.statSync(filePath).isFile()
        fs.unlinkSync filePath
        console.log "Deleted ".red + filePath
      else
        rmDir filePath
        fs.rmdirSync filePath
      i++

task 'clean', 'remove everything from "assets/generated" and all .pyc and ~ files', ->
    rmDir css_out+"/"
    rmDir js_out+"/"
    exec "find . -name \*.pyc -delete", (error, stdout, stderr) ->
        console.log stdout
    exec "find . -name '*~' -delete", (error, stdout, stderr) ->
        console.log stdout

task 'develop', 'recompile, watch, and run the server', ->
    watch_files = true
    invoke 'less'
    invoke 'coffee'

task 'build', 'recompile, all assets', ->
    invoke 'less'
    invoke 'coffee'

task 'less', ->
    compile_recursive less_src, css_out, "less", "css"

task 'coffee', ->
    compile_recursive coffe_src, js_out, "coffee", "js"