

# Git is a VCS (Version Control System) and keeps tracks of your code
# Github online platform that stores our projects



# Git Flow


# 1. Initialize the git => git init ( Only once for a project )
# U => Untracked
# A => Added
# M => Modified
# 2. Connect your project folder with github repository => git remote add origin {ssh_key} ( Only once for a project )
# 3. Add files in git => git add {file_name} // git add .
# 4. Commit the changes => git commit -m "Message" => It prepares the git to push to the github and saves the content
# 5. Push the code into github => git push -u origin {branch_name} (It is recommended that the first push should be done by adding upstream)
# git push origin {branch_name} => This is most recommended way
# -u => Upstream => Upstream saves the branch . We donot need to specify the branch while pushing to github once we set the upstream
# Then we need to do git push => it pushes directlt to the upstream branch



# Branching allows multiple collaboraters work on a same project


# To create a branch => git branch {branch_name} // git checkout -b {branch__name}
# To view the branches => git branch // git branch -a
# To change the branch => git switch {branch_name}
# To pull content from github => git pull origin {branch_name}
# Merging the content => git merge {branch_name}